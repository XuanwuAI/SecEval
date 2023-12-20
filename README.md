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

| #   | Model              | Creator       | Access   | Submission Date | System Security | PenTest | Network Security | Application Security | Web Security | Vulnerability | Software Security | Memory Safety | Cryptography | Overall |
|-----|--------------------|---------------|----------|-----------------|-----------------|---------|------------------|----------------------|--------------|-----------------|--------------------|--------------|--------------|---------|
| 1   | gpt-35-turbo       | OpenAI        | API, Web | 2023-12-20      | 50.55           | 67.09   | 52.57            | 49.53                | 58.13        | 51.86           | 48.60              | 35.21        | 38.89        | 51.34   |
| 2   | Yi-6B              | 01-ai         | Weight   | 2023-12-20      | 43.46           | 60.94   | 52.21            | 41.96                | 48.70        | 42.15           | 38.48              | 30.99        | 33.33        | 45.00   |
| 3   | chatglm3-6b-base   | THUDM         | Weight   | 2023-12-20      | 34.81           | 50.27   | 38.97            | 32.71                | 37.20        | 31.82           | 33.99              | 25.35        | 27.78        | 35.61   |
| 4   | internlm-7b        | internlm      | Weight   | 2023-12-20      | 21.95           | 31.65   | 26.47            | 21.59                | 29.22        | 25.21           | 28.65              | 21.13        | 16.67        | 25.40   |
| 5   | Llama-2-7b-hf      | MetaAI        | Weight   | 2023-12-20      | 17.96           | 22.97   | 12.87            | 16.26                | 19.38        | 17.98           | 17.70              | 16.90        | 22.22        | 18.46   |
| 6   | Atom-7B            | FlagAlpha     | Weight   | 2023-12-20      | 16.04           | 22.24   | 14.34            | 14.58                | 20.62        | 16.94           | 18.26              | 12.68        | 27.78        | 17.64   |

## Dataset

You can download the json file of the dataset by running.

```
wget https://huggingface.co/datasets/XuanwuAI/SecEval/blob/main/problems.json
```

Or you can load the dataset from [Huggingface](https://huggingface.co/datasets/XuanwuAI/SecEval).

## Evaluate

You can use our [evaluation script](https://github.com/XuanwuAI/SecEval/tree/main/eval) to evaluate your model on SecEval dataset.


## Paper

Comming Soon

## Limitations

The dataset, while comprehensive, exhibits certain constraints:

1. **Distribution Imbalance**: The dataset presents an uneven distribution of questions across different domains, resulting in a higher concentration of questions in certain areas while others are less represented.

2. **Incomplete Scope**: Some topics on Cybersecurity are absent from the dataset, such as content security, reverse engineering, and malware analysis. As such, it does not encapsulate the full breadth of knowledge within the field.

3. **Accuracy Concerns**: A minor fraction of the questions have been identified as incorrect during sample inspections. These inaccuracies stem from limitations inherent in the current generation methodology. **However, these inaccuracies are sufficiently infrequent to not influence the effectiveness of the dataset.**

## Future Work

1. **Improvement on Distribution**: We aim to broaden the dataset's comprehensiveness by incorporating additional questions, thereby enriching the coverage of existing cybersecurity topics.

2. **Improvement on Topic Coverage**: Efforts will be made to include a wider array of cybersecurity topics within the dataset, which will help achieve a more equitable distribution of questions across various fields.

3. **Quality Assurance**: We plan to implement a robust verification pipeline to ensure the correctness of each question within the dataset. (Doing)


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