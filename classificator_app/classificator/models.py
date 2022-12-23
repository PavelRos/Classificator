import pandas as pd
import nltk
# nltk.download()
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from pickle import dump, load
from classificator_app.settings import MODEL_PATH

# Create your models here.


class Svc_model:

    def __init__(self, model, vect, transformer):
        self.svclassifier = model
        self.transformer = transformer
        self.vectorizer = vect

    @classmethod
    def prepareText(cls, text: str):
        tokenizer = RegexpTokenizer("\w+")
        words = tokenizer.tokenize(text.lower())
        significant_words = [
            word for word in words if word not in stopwords.words("russian")
        ]
        lemmatizer = WordNetLemmatizer()
        lemms = [lemmatizer.lemmatize(word) for word in significant_words]
        return " ".join(lemms)
