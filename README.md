# SecEval: A Comprehensive Benchmark for Evaluating Cybersecurity Knowledge of Foundation Models

## About SecEval

SecEval is the first benchmark specifically created for evaluating cybersecurity knowledge in Foundation Models. It offers over 2000 multiple-choice questions across 9 domains: Software Security, Application Security, System Security, Web Security, Cryptography, Memory Safety, Network Security, and PenTest.
SecEval generates questions by prompting OpenAI GPT4 with authoritative sources such as open-licensed textbooks, official documentation, and industry guidelines and standards. The generation process is meticulously crafted to ensure the dataset meets rigorous quality, diversity, and impartiality criteria. You can explore our dataset the [explore page](https://xuanwuai.github.io/SecEval/explore.html). 



## Table of Contents

- [Leaderboard](#leaderboard)
- [Dataset](#dataset)
- [Evaluate](#evaluate)
- [Paper](#paper)
- [Limitations](#limitations)
- [Future Work](#future-work)
- [Licenses](#licenses)
- [Citation](#citation)



## Leaderboard

| #   | Model              | Creator    | Access | Submission Date | System Security | PenTest | Network Security | Application Security | Web Security | Vulnerability | Software Security | Memory Safety | Cryptography | Overall |
|-----|--------------------|------------|--------|-----------------|-----------------|---------|------------------|----------------------|--------------|-----------------|------------------|--------------|--------------|---------|
| 1   | gpt-35-turbo       | OpenAI     | API, Web | 2023-12-20      | 51.0            | 67.0    | 53.0             | 50.0                 | 58.0         | 52.0            | 49.0             | 35.0         | 39.0         | 0.51    |
| 2   | Yi-6B              | 01-ai      | Weight | 2023-12-20      | 43.0            | 61.0    | 52.0             | 42.0                 | 49.0         | 42.0            | 38.0             | 31.0         | 33.0         | 0.45    |
| 3   | chatglm3-6b-base   | THUDM      | Weight | 2023-12-20      | 35.0            | 50.0    | 39.0             | 33.0                 | 37.0         | 32.0            | 34.0             | 25.0         | 28.0         | 0.36    |
| 4   | internlm-7b        | internlm   | Weight | 2023-12-20      | 22.0            | 32.0    | 26.0             | 22.0                 | 29.0         | 25.0            | 29.0             | 21.0         | 17.0         | 0.25    |
| 5   | Atom-7B            | FlagAlpha  | Weight | 2023-12-20      | 16.0            | 22.0    | 14.0             | 15.0                 | 21.0         | 17.0            | 18.0             | 13.0         | 28.0         | 0.18    |
| 6   | Llama-2-7b-hf      | MetaAI     | Weight | 2023-12-20      | 18.0            | 23.0    | 13.0             | 16.0                 | 19.0         | 18.0            | 18.0             | 17.0         | 22.0         | 0.18    |


## Dataset

You can download the json file of the dataset by running.

```
wget https://huggingface.co/datasets/XuanwuAI/SecEval/blob/main/problems.json
```

Or you can load the dataset from [Huggingface](https://huggingface.co/datasets/XuanwuAI/SecEval).

## Evaluate

You can use our [evaluation script](eval/README.md) your model on SecEval dataset.


## Paper

Comming Soon

## Limitations

The dataset, while comprehensive, exhibits certain constraints:

1. **Distribution Imbalance**: The dataset presents an uneven distribution of questions across different domains, resulting in a higher concentration of questions in certain areas while others are less represented.

2. **Incomplete Scope**: Notably absent from the dataset are topics pertaining to cybersecurity, such as content security, reverse engineering, and malware analysis. As such, it does not encapsulate the full breadth of knowledge within the field.

3. **Accuracy Concerns**: A minor fraction of the questions have been identified as incorrect during sample inspections. These inaccuracies stem from limitations inherent in the current generation methodology. **However, these inaccuracies are sufficiently infrequent to not influence the effectiveness of the dataset.**

## Future Work

1. **Improvement on Distribution**: We aim to broaden the dataset's comprehensiveness by incorporating additional questions, thereby enriching the coverage of existing cybersecurity topics.

2. **Improvement on Topic Coverage**: Efforts will be made to include a wider array of cybersecurity topic within the dataset, which will help achieve a more equitable distribution of questions across various fields.

3. **Quality Assurance**: We plan to implement a robust verification pipeline to ensure the correctness of each question within the dataset. (Doing)


## Licenses

The dataset is released under the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license. The code is released under the [MIT](https://opensource.org/licenses/MIT) license.


## Citation

```bibtex
@misc{li2023seceval,
    title={SecEval: A Comprehensive Benchmark for Evaluating Cybersecurity Knownledge of Foundation Models},
    author={Li, Guancheng and Li, Yifeng and Wang Guannan and Yang, Haoyu and Yu, Yang},
    publisher = {GitHub},
    howpublished= "https//github.com/XuanwuAI/SecEval",
    year={2023}
}
```