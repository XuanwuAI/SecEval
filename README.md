# SecEval: A Comprehensive Benchmark for Evaluating Cybersecurity Knowledge of Foundation Models

[中文版](README_CN.md).

The advent of large language models has ignited a transformative era for the cybersecurity industry. Pioneering applications are being developed, deployed, and utilized in areas such as cybersecurity knowledge QA, vulnerability hunting, and alert investigation. Various researches have indicated that LLMs primarily acquire their knowledge during the pretraining phase, with fine-tuning serving essentially to align the model with user intentions, providing the ability to follow instructions. This suggests that the knowledge and skills embedded in the foundational model significantly influence the model's potential on specific downstream tas ks

Yet, a focused evaluation of cybersecurity knowledge is missing in existing datasets. We address this by introducing "SecEval". SecEval is the first benchmark specifically created for evaluating cybersecurity knowledge in Foundation Models. It offers over 2000 multiple-choice questions across 9 domains: Software Security, Application Security, System Security, Web Security, Cryptography, Memory Safety, Network Security, and PenTest.
SecEval generates questions by prompting OpenAI GPT4 with authoritative sources such as open-licensed textbooks, official documentation, and industry guidelines and standards. The generation process is meticulously crafted to ensure the dataset meets rigorous quality, diversity, and impartiality criteria. You can explore our dataset the [explore page](https://xuanwuai.github.io/SecEval/explore.html). 

Using SecEval, we conduct an evaluation of 10 state-of-the-art foundational models, providing new insights into their performance in the field of cybersecurity. The results indicate that there is still a long way to go before LLMs can be the master of  cybersecurity. We hope that SecEval can serve as a catalyst for future research in this area.



## Table of Contents

- [Leaderboard](#leaderboard)
- [Dataset](#dataset)
- [Generation Process](#generation-process)
- [Limitations](#limitations)
- [Future Work](#future-work)
- [Licenses](#licenses)
- [Citation](#citation)
- [Credits](#credits)



## Leaderboard

| #   | Model             | Creator   | Access    | Submission Date | System Security | Application Security | PenTest | Memory Safety | Network Security | Web Security | Vulnerability | Software Security | Cryptography | Overall |
|-----|-------------------|-----------|-----------|-----------------|-----------------|----------------------|---------|---------------|------------------|--------------|---------------|-------------------|--------------|---------|
| 1   | GPT-4-turbo       | OpenAI    | API, Web  | 2023-12-20      | 73.61           | 75.25                | 80.00   | 70.83         | 75.65            | 82.15        | 76.05         | 73.28             | 64.29        | 79.07   |
| 2   | gpt-3.5-turbo     | OpenAI    | API, Web  | 2023-12-20      | 59.15           | 57.18                | 72.00   | 43.75         | 60.87            | 63.00        | 60.18         | 58.19             | 35.71        | 62.09   |
| 3   | Yi-6B             | 01-AI     | Weight    | 2023-12-20      | 50.61           | 48.89                | 69.26   | 35.42         | 56.52            | 54.98        | 49.40         | 45.69             | 35.71        | 53.57   |
| 4   | Orca-2-7b         | Microsoft | Weight    | 2023-12-20      | 46.76           | 47.03                | 60.84   | 31.25         | 49.13            | 55.63        | 50.00         | 52.16             | 14.29        | 51.60   |
| 5   | Mistral-7B-v0.1   | Mistralai | Weight    | 2023-12-20      | 40.19           | 38.37                | 53.47   | 33.33         | 36.52            | 46.57        | 42.22         | 43.10             | 28.57        | 43.65   |
| 6   | chatglm3-6b-base  | THUDM     | Weight    | 2023-12-20      | 39.72           | 37.25                | 57.47   | 31.25         | 43.04            | 41.14        | 37.43         | 39.66             | 28.57        | 41.58   |
| 7   | Aquila2-7B        | BAAI      | Weight    | 2023-12-20      | 34.84           | 36.01                | 47.16   | 22.92         | 32.17            | 42.04        | 38.02         | 36.21             | 7.14         | 38.29   |
| 8   | Qwen-7B           | Alibaba   | Weight    | 2023-12-20      | 28.92           | 28.84                | 41.47   | 18.75         | 29.57            | 33.25        | 31.74         | 30.17             | 14.29        | 31.37   |
| 9   | internlm-7b       | Sensetime | Weight    | 2023-12-20      | 25.92           | 25.87                | 36.21   | 25.00         | 27.83            | 32.86        | 29.34         | 34.05             | 7.14         | 30.29   |
| 10  | Llama-2-7b-hf     | MetaAI    | Weight    | 2023-12-20      | 20.94           | 18.69                | 26.11   | 16.67         | 14.35            | 22.77        | 21.56         | 20.26             | 21.43        | 22.15   |

## Dataset

### Format

The dataset is in json format. Each question has the following fields:

* id: str # unique id for each question
* source: str # the source where the question is generated from
* question: str # the question description
* choices: List[str] # the choices for the question
* answer: str # the answer for the question
* topics: List[QuestionTopic] # the topics for the question, each question can have multiple topics.
* keyword: str # the keyword for the question


### Question Distribution

| Topic               | No. of Questions |
|---------------------|-----------------|
| SystemSecurity      | 1065            |
| ApplicationSecurity | 808             |
| PenTest             | 475             |
| MemorySafety        | 48              |
| NetworkSecurity     | 230             |
| WebSecurity         | 773             |
| Vulnerability       | 334             |
| SoftwareSecurity    | 232             |
| Cryptography        | 14              |
| Overall             | 2126            |


### Download
You can download the json file of the dataset by running.

```
wget https://huggingface.co/datasets/XuanwuAI/SecEval/blob/main/questions.json
```

Or you can load the dataset from [Huggingface](https://huggingface.co/datasets/XuanwuAI/SecEval).

### Evaluate Your Model on SecEval 

You can use our [evaluation script](https://github.com/XuanwuAI/SecEval/tree/main/eval) to evaluate your model on SecEval dataset.


## Generation Process

### Data Collection

- **Textbook**: We selected open-licensed textbooks from the Computer Security courses CS161 at UC Berkeley and 6.858 at MIT. These resources provide extensive information on network security, memory safety, web security, and cryptography. 

- **Official Documentation**: We utilized official documentation, such as Apple Platform Security, Android Security, and Windows Security, to integrate system security and application security knowledge specific to these platforms.

- **Industrial Guidelines**: To encompass web security, we referred to the Mozilla Web Security Guidelines. In addition, we used the OWASP Web Security Testing Guide (WSTG) and OWASP Mobile Application Security Testing Guide (MASTG) for insights into web and application security testing.

- **Industrial Standards**: The Common Weakness Enumeration (CWE) was employed to address knowledge of vulnerabilities. For penetration testing, we incorporated the MITRE ATT&CK and MITRE D3fend frameworks.

### Questions Generation

To facilitate the evaluation process, we designed the dataset in a multiple-choice question format. Our approach to question generation involved several steps:

1. **Text Parsing**: We began by parsing the texts according to their hierarchical structure, such as chapters and sections for textbooks, or tactics and techniques for frameworks like ATT&CK.

2. **Content Sampling**: For texts with extensive content, such as CWE or Windows Security Documentation, we employed a sampling strategy to maintain manageability. For example, we selected the top 25 most common weakness types and 175 random types from CWE. 

3. **Question Generation**: Utilizing GPT-4, we generated multiple-choice questions based on the parsed text, with the level of detail adjusted according to the content's nature. For instance, questions stemming from the CS161 textbook were based on individual sections, while those from ATT&CK were based on techniques.

4. **Question Refinement**: We then prompted GPT-4 to identify and filter out questions with issues such as too simplistic or not self-contained. Where possible, questions were revised; otherwise, they were discarded.

5. **Answer Calibration**: We refine the selection of answer options by presenting GPT-4 with both the question and the source text from which the question is derived. Should the response generated by GPT-4 diverge from the previously established answer, this discrepancy suggests that obtaining a consistent answer for the question is inherently challenging. In such cases, we opt to eliminate these problematic questions. 

6. **Classification**: Finally, we organized the questions into 9 topics, and attached a relevant fine-grained keyword to each question.


## Limitations

The dataset, while comprehensive, exhibits certain constraints:

1. **Distribution Imbalance**: The dataset presents an uneven distribution of questions across different domains, resulting in a higher concentration of questions in certain areas while others are less represented.

2. **Incomplete Scope**: Some topics on Cybersecurity are absent from the dataset, such as content security, reverse engineering, and malware analysis. As such, it does not encapsulate the full breadth of knowledge within the field.

## Future Work

1. **Improvement on Distribution**: We aim to broaden the dataset's comprehensiveness by incorporating additional questions, thereby enriching the coverage of existing cybersecurity topics.

2. **Improvement on Topic Coverage**: Efforts will be made to include a wider array of cybersecurity topics within the dataset, which will help achieve a more equitable distribution of questions across various fields.


## Licenses

The dataset is released under the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license. The code is released under the [MIT](https://opensource.org/licenses/MIT) license.


## Citation

```bibtex
@misc{li2023seceval,
    title={SecEval: A Comprehensive Benchmark for Evaluating Cybersecurity Knowledge of Foundation Models},
    author={Li, Guancheng and Li, Yifeng and Wang Guannan and Yang, Haoyu and Yu, Yang},
    publisher = {GitHub},
    howpublished= "https://github.com/XuanwuAI/SecEval",
    year={2023}
}
```

## Credits

This work is supported by [Tencent Security Xuanwu Lab](https://xlab.tencent.com/en/). we also apperiate Tencent Spark Talent Program for help.