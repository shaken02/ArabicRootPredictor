# Arabic Root Predictor

This repository provides a pre-trained machine learning model for predicting the root of Arabic words.
You should install two models that are needed to perform this task: vectorizer and predictor models. They can be downloaded by the link - https://drive.google.com/drive/u/1/folders/1IgfkpU5SyoLoZ2TvheuiNGqLvp1VKXpB.

## Usage

To predict the root of an Arabic word, run `predict.py` file.


## Model Details

- The model is trained using `scikit-learn`.
- It uses a vectorizer for feature extraction.
- Uses 15 trees in the Random Forest.
- 81% accuracy.
