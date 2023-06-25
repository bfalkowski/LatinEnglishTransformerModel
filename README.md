
## Latin-to-English Transformer Model using CCMatrix

This repository contains a Transformer model trained to perform Latin-to-English translation using the extensive CCMatrix dataset. CCMatrix is a large-scale collection of high-quality parallel sentences extracted from the CommonCrawl public dataset, encompassing more than 4.5 billion sentence pairs in 576 language pairs. By leveraging this massive corpus, our model offers an efficient and accurate solution for Latin translation tasks.

### Features:
- **Transformer Architecture**: The model is based on the Transformer architecture, which has demonstrated remarkable success in various natural language processing tasks, including machine translation.
- **CCMatrix Dataset**: The model is trained on the Latin-to-English sentence pairs sourced from the CCMatrix dataset. This enables the model to learn robust translation patterns and produce high-quality translations.



Code Derived from https://github.com/hkproj/pytorch-transformer 

## Dataset Description

- Homepage: https://opus.nlpl.eu/CCMatrix.php
- Sample: https://opus.nlpl.eu/CCMatrix/v1/en-la_sample.html
- Paper: https://arxiv.org/abs/1911.04944

The latin dataset contans:
    - 1,114,190 Sentance pairs
    - 14.5 M words

## Huggingface
- README: https://huggingface.co/datasets/yhavinga/ccmatrix/blob/main/README.md
- DATASET: https://huggingface.co/datasets/yhavinga/ccmatrix/viewer/en-la/train


### Data Format
```
{
        "id": 1,
        "score": 1.2498379,
        "translation": {
            "en": "No telling what sort of magic he might have.\""
            "la": "numque magistrâtum cum iis habent.\
        },
        "id": 2,
        "score": 1.1443379,
        "translation": {
            "en": "Not many, but much.\""
            "la": "non multa sed multum.\
        }
    }
```

