# Evaluating on SecEval Dataset

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Download Dataset



## Evaluate on a Model

### Usage

```bash
usage: eval.py [-h] [-o OUTPUT_DIR] -d DATASET_FILE [-c] [-b BATCH_SIZE] -B {remote_hf,azure,textgen,local_hf} -m MODELS [MODELS ...]

SecEval Evaluation CLI

options:
  -h, --help            show this help message and exit
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
                        Specify the output directory.
  -d DATASET_FILE, --dataset_file DATASET_FILE
                        Specify the dataset file to evaluate on.
  -c, --chat            Evaluate on chat model.
  -b BATCH_SIZE, --batch_size BATCH_SIZE
                        Specify the batch size.
  -B {remote_hf,azure,textgen,local_hf}, --backend {remote_hf,azure,textgen,local_hf}
                        Specify the llm type. remote_hf: remote huggingface model backed, azure: azure openai model, textgen: textgen backend, local_hf: local huggingface model backed
  -m MODELS [MODELS ...], --models MODELS [MODELS ...]
                        Specify the models.
```

### Select a Backend 

There are four backends supported for evaluating on SecEval dataset.
Some backends require additional environment variables to be set.

#### Local Huggingface Model Backend

Local Huggingface Model Backend is used for evaluating on models that are stored locally. You can download the models from [Huggingface](https://huggingface.co/models) and use this backend to evalute the model.

```bash
export HF_LOCAL_MODEL_DIR=<path to local huggingface model>
```

#### Remote Huggingface Model Backend

Remote Huggingface Model Backend is used for evaluating on models that are stored on Huggingface. You can use this backend to evalute the model.


#### Azure OpenAI Model Backend

Azure OpenAI Model Backend is used for evaluating on models that are deployed on Azure OpenAI. 

```bash
export OPENAI_API_KEY=<your openai api key>
export OPENAI_API_ENDPOINT=<your openai api endpoint>
export OPENAI_MODEL_NAME=<your openai model name>
```


#### text-generation-webui Backend

[text-generation-webui](https://github.com/oobabooga/text-generation-webui) is a service used for deploying and testing models. We have supported evaluating on models deployed on text-generation-webui.

```bash

export TEXTGEN_MODEL_URL=<your textgenerationwebui api url>
```

### Run Evaluation

If you want to evaluate on a base model, you can run the following command:

```bash
python eval.py -d <path to dataset file> -B <backend> -m <model name> -o <output directory>
```

If you want to evaluate on a chat model such as gpt-3.5-turbo, you should add the `-c` flag:

```bash 
python eval.py -d <path to dataset file> -B <backend> -m <model name> -o <output directory> -c
```


## Inspection the Results

The results will be saved in the output directory. The result is a JSONObject contains following field

```json
{
    "score_fraction": {
        "topic_name": "topic_score_fraction",
    },
    "score_float": {
        "topic_name": "topic_score_float",
    },
    "detail": ["detail1", "detail2",] 
}
```