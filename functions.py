# importing libraries
import pandas as pd
import re
import string
import nltk
import pickle
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from nltk.tokenize import RegexpTokenizer
from nltk import PorterStemmer, WordNetLemmatizer

nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("stopwords")

# preprocessing functions


# converting tweet text to lower case
def text_lower(text):
    return text.str.lower()


# removing stopwoords from the tweet text
def clean_stopwords(text):
    # stopwords list that needs to be excluded from the data
    stopwordlist = set(stopwords.words("english"))
    STOPWORDS = set(stopwordlist)
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])


# cleaning and removing punctuations
def clean_puctuations(text):
    english_puctuations = string.punctuation
    translator = str.maketrans("", "", english_puctuations)
    return text.translate(translator)


# cleaning and removing repeating characters
def clean_repeating_characters(text):
    return re.sub(r"(.)1+", r"1", text)


# cleaning and removing URLs
def clean_URLs(text):
    return re.sub(r"((www.[^s]+)|(http\S+))", "", text)


# cleaning and removing numeric data
def clean_numeric(text):
    return re.sub("[0-9]+", "", text)


# Tokenization of tweet text
def tokenize_tweet(text):
    tokenizer = RegexpTokenizer("\w+")
    text = text.apply(tokenizer.tokenize)
    return text


# stemming
def text_stemming(text):
    st = PorterStemmer()
    text = [st.stem(word) for word in text]
    return text


# lemmatization
def text_lemmatization(text):
    lm = WordNetLemmatizer()
    text = [lm.lemmatize(word) for word in text]
    return text


# defining preprocess function


def preprocess(text):
    text = text_lower(text)
    text = text.apply(lambda text: clean_stopwords(text))
    text = text.apply(lambda x: clean_puctuations(x))
    text = text.apply(lambda x: clean_repeating_characters(x))
    text = text.apply(lambda x: clean_URLs(x))
    text = text.apply(lambda x: clean_numeric(x))
    text = tokenize_tweet(text)
    text = text.apply(lambda x: text_stemming(x))
    text = text.apply(lambda x: text_lemmatization(x))
    text = text.apply(lambda x: " ".join(x))
    return text


# Function for custom input prediction
def custom_input_prediction(text):
    import nltk

    nltk.download("omw-1.4")
    text = pd.Series(text)
    text = preprocess(text)
    text = [
        text[0],
    ]
    vectoriser = pickle.load(open("tdf_vectorizer", "rb"))
    text = vectoriser.transform(text)
    model = pickle.load(open("model.bin", "rb"))
    prediction = model.predict(text)
    prediction = prediction[0]

    interpretations = {
        0: "Age",
        1: "Ethnicity",
        2: "Gender",
        3: "Not Cyberbullying",
        4: "Religion",
    }

    for i in interpretations.keys():
        if i == prediction:
            return interpretations[i]
