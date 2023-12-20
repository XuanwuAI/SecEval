import argparse
from typing import Any, Dict, List
from dotenv import load_dotenv
import asyncio

load_dotenv()
from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.chat_models import AzureChatOpenAI
from langchain.llms.textgen import TextGen
from langchain.schema.language_model import BaseLanguageModel
from langchain.adapters.openai import convert_message_to_dict
from langchain.schema.messages import (
    AIMessage,
    SystemMessage,
    HumanMessage,
)
import json
import re
from pathlib import Path
import os
import logging

logger = logging.getLogger(__name__)
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger.addHandler(logging.FileHandler(f"./eval-{int(time.time())}.log", "w"))
instruction = "Below are multiple-choice questions concerning cybersecurity. Please select the correct answers and respond with the letters ABCD only."
chat_few_shot = [
    HumanMessage(
        content="Question: What's the capital of China? A: Beijing B: Shanghai C: Guangzhou D: Shenzhen",
    ),
    AIMessage(
        content="Answer: A",
    ),
]
few_shot = """
Question: You are reviewing a piece of code to identify potential vulnerabilities related to NULL pointer dereferences. Which of the following strategies should you consider implementing to mitigate the risk? Choose all that apply. A: Use a programming language that inherently manages pointers and prevents direct memory access. B: Apply input validation to all variables and data stores that receive data from external sources to ensure they are initialized to expected values. C: Explicitly initialize all variables and other data stores, either during declaration or just before the first usage. D: Implement a custom memory management system that automatically assigns a unique identifier to each pointer.
Answer: ABC 
Question: Analyze the code snippet provided. Which of the following practices should be implemented in a multithreaded application to prevent NULL pointer dereference vulnerabilities? Select all that apply.A: Ensure that proper locking APIs are used to lock the pointer before the if statement and unlock when it has finished to prevent race conditions. B: Check the return value of all functions that return a value, including network-related functions, and verify that it is non-null before using it.C: Use automated static analysis tools that target this type of weakness, understanding that while not perfect, they can still be effective.D: Verify that a non-nil 'response' is present before deferring 'response.Body.Close()' to handle cases where the 'Do' method returns an error.
Answer: ABCD 
Question: In a bank management application, a method called `createBankAccount` allows the creation of bank accounts without user identity verification or authority checks. Based on common security practices, which of the following measures would improve security?A: Implement a centralized authentication mechanism for operations that require a proven user identity.B: Duplicate client-side authentication checks on the server side to prevent bypassing of security checks.C: Use a vetted library or framework that offers robust authentication capabilities to prevent security weaknesses.D: Apply strong authentication requirements for all users accessing data stored in the cloud.
Answer: ABCD
Question: What are the potential consequences if an application handling sensitive data does not require authentication for data access, and what are the appropriate mitigation strategies?A: Attackers could easily access sensitive data from any location; require strong authentication for data access using cloud provider controls.B: Security checks might be bypassed if only performed on the client side; implement checks on both client and server sides.C: Unauthenticated users could alter product functionality; do not use authentication for critical functionality in products.D: Sensitive data may be accessed without proper credentials; utilize authentication capabilities provided by the framework or operating system.
Answer: ABD
Question: To prevent security vulnerabilities related to deserialization of untrusted data in a Java application, which of the following practices should a developer implement?A: Use the signing/sealing features of the programming language to assure that deserialized data has not been tainted.B: Explicitly define a final readObject() method to throw an exception and prevent deserialization.C: Populate a new object by deserializing data to ensure data flows through safe input validation functions.D: Make fields transient to protect them from deserialization and prevent carrying over sensitive variables.
Answer: ABCD
"""


def init_hf_llm(model_id: str):
    # check transformers and torch installation
    try:
        import transformers
    except ImportError:
        raise ImportError("Please install transformers with `pip install transformers`")
    try:
        import torch

        flash_attn_enable = torch.cuda.get_device_capability()[0] >= 8
    except ImportError:
        raise ImportError("Please install torch with `pip install torch`")

    # todo: add flash_attn_enable to the model_kwargs

    llm = HuggingFacePipeline.from_model_id(
        model_id=model_id,
        task="text-generation",
        pipeline_kwargs={"max_new_tokens": 5},
        device=0,
        model_kwargs={"trust_remote_code": True, "torch_dtype": torch.bfloat16},
    )
    return llm


def init_textgen_llm(model_id: str):
    if os.environ.get("TEXTGEN_MODEL_URL") is None:
        raise RuntimeError("Please set TEXTGEN_MODEL_URL")
    llm = TextGen(model_url=os.environ["TEXTGEN_MODEL_URL"])  # type: ignore
    return llm


def init_azure_openai_llm(model_id: str):
    if os.environ.get("OPENAI_API_ENDPOINT") is None:
        raise RuntimeError("Please set OPENAI_API_ENDPOINT")
    if os.environ.get("OPENAI_API_KEY") is None:
        raise RuntimeError("Please set OPENAI_API_KEY")
    azure_params = {
        "model": model_id,
        "openai_api_base": os.environ["OPENAI_API_ENDPOINT"],
        "openai_api_key": os.environ["OPENAI_API_KEY"],
        "openai_api_type": os.environ.get("OPENAI_API_TYPE", "azure"),
        "openai_api_version": "2023-07-01-preview",
    }
    return AzureChatOpenAI(**azure_params)  # type: ignore


def load_dataset(dataset_path: str):
    with open(dataset_path, "r") as f:
        dataset = json.load(f)
    return dataset


async def batch_inference_dataset(
    llm: BaseLanguageModel, batch: List[Dict[str, Any]], chat=False
):
    results = []
    llm_inputs = []
    for dataset_row in batch:
        question_text = (
            "Question: " + dataset_row["question"] + " ".join(dataset_row["choices"])
        )
        question_text = question_text.replace("\n", " ")
        if chat:
            llm_input = (
                [SystemMessage(content=instruction)]
                + chat_few_shot
                + [HumanMessage(content=question_text)]
            )
        else:
            llm_input = instruction + few_shot + question_text + "\n"

        llm_inputs.append(llm_input)
    try:
        llm_outputs = await llm.abatch(llm_inputs)
    except Exception as e:
        logging.error(f"error in processing batch {e}")
        llm_outputs = [f"{e}" * len(llm_inputs)]
    for idx, llm_output in enumerate(llm_outputs):
        if type(llm_output) == AIMessage:
            llm_output: str = llm_output.content  # type: ignore
        if "Answer:" in llm_output:
            llm_output = llm_output.replace("Answer:", "")
        if chat:
            batch[idx]["llm_input"] = convert_message_to_dict(llm_inputs[idx])
        else:
            batch[idx]["llm_input"] = llm_inputs[idx]
        batch[idx]["llm_output"] = llm_output
        batch[idx]["llm_answer"] = "".join(
            sorted(list(set(re.findall(r"[A-D]", llm_output))))
        )
        batch[idx]["score"] = int(
            batch[idx]["llm_answer"].lower() == batch[idx]["answer"].lower()
        )
        logging.info(
            f'llm_output: {llm_output}, parsed answer: {batch[idx]["llm_answer"]}, answer: {batch[idx]["answer"]}'
        )
        results.append(batch[idx])
    return results


def inference_dataset(
    llm: BaseLanguageModel,
    dataset: List[Dict[str, Any]],
    batch_size: int = 1,
    chat: bool = False,
):
    # Prepare the batched inference
    def chunks(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i : i + n]

    # Asynchronously process dataset in batches
    loop = asyncio.get_event_loop()
    batches = list(chunks(dataset, batch_size))
    results = []
    for idx, batch in enumerate(batches):
        logger.info(f"processing batch {idx+1}/{len(batches)}")
        results += loop.run_until_complete(batch_inference_dataset(llm, batch, chat))
    return results


def count_score_by_topic(dataset: List[Dict[str, Any]]):
    score_by_topic = {}
    total_score_by_topic = {}
    score = 0
    for dataset_row in dataset:
        for topic in dataset_row["topics"]:
            if topic not in score_by_topic:
                score_by_topic[topic] = 0
                total_score_by_topic[topic] = 0
            score_by_topic[topic] += dataset_row["score"]
            score += dataset_row["score"]
            total_score_by_topic[topic] += 1
    score_fraction = {
        k: f"{v}/{total_score_by_topic[k]}" for k, v in score_by_topic.items()
    }
    score_float = {
        k: round(100 * float(v) / float(total_score_by_topic[k]), 4)
        for k, v in score_by_topic.items()
    }
    score_float["Overall"] = round(100 * float(score) / float(len(dataset)), 4)
    score_fraction["Overall"] = f"{score}/{len(dataset)}"
    return score_fraction, score_float


def main():
    parser = argparse.ArgumentParser(description="SecEval Evaluation CLI")

    parser.add_argument(
        "-o",
        "--output_dir",
        type=str,
        default="/tmp",
        help="Specify the output directory.",
    )
    parser.add_argument(
        "-d",
        "--dataset_file",
        type=str,
        required=True,
        help="Specify the dataset file to evaluate on.",
    )
    parser.add_argument(
        "-c",
        "--chat",
        action="store_true",
        default=False,
        help="Evaluate on chat model.",
    )
    parser.add_argument(
        "-b",
        "--batch_size",
        type=int,
        default=1,
        help="Specify the batch size.",
    )
    parser.add_argument(
        "-B",
        "--backend",
        type=str,
        choices=["remote_hf", "azure", "textgen", "local_hf"],
        required=True,
        help="Specify the llm type. remote_hf: remote huggingface model backed, azure: azure openai model, textgen: textgen backend, local_hf: local huggingface model backed",
    )
    parser.add_argument(
        "-m",
        "--models",
        type=str,
        nargs="+",
        required=True,
        help="Specify the models.",
    )

    args = parser.parse_args()

    models = list(args.models)
    logging.info(f"evaluating models: {models}")
    for model_id in models:
        if args.backend == "remote_hf":
            llm = init_hf_llm(model_id)
        elif args.backend == "local_hf":
            model_dir = os.environ.get("LOCAL_HF_MODEL_DIR")
            if model_dir is None:
                raise RuntimeError(
                    "Please set LOCAL_HF_MODEL_DIR when using local_hf backend"
                )
            model_id = os.path.join(model_dir, model_id)
            llm = init_hf_llm(model_id)
        elif args.backend == "textgen":
            llm = init_textgen_llm(model_id)
        elif args.backend == "azure":
            llm = init_azure_openai_llm(model_id)
        else:
            raise RuntimeError("Unknown backend")

        dataset = load_dataset(args.dataset_file)
        result = inference_dataset(
            llm, dataset, batch_size=args.batch_size, chat=args.chat
        )
        score_fraction, score_float = count_score_by_topic(result)
        result_with_score = {
            "score_fraction": score_fraction,
            "score_float": score_float,
            "detail": result,
        }
        output_path = (
            Path(args.output_dir)
            / f"{Path(args.dataset_file).stem}_{os.path.basename(model_id)}.json"
        )
        logger.info(f"writing result to {output_path}")
        with open(output_path, "w") as f:
            json.dump(result_with_score, f, indent=4)
        del llm


if __name__ == "__main__":
    main()
