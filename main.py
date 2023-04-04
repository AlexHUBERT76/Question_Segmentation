# text preprocessing modules
from string import punctuation 
# text preprocessing modules
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re  # regular expression
import os
from os.path import dirname, join, realpath
import joblib
import uvicorn
from fastapi import FastAPI
import tensorflow_hub as hub

app = FastAPI(
    title="Topics Model API",
    description="A simple API that use NLP model to predict the topics of a stack overflow post",
    version="0.1",
)

# load the sentiment model
PATHGit = r"./"

model = joblib.load(os.path.join(PATHGit,'best_model.joblib'))


#importing USE model
module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
USE_model = hub.load(module_url)


#importing binarizer decoder model
binarizer = joblib.load(os.path.join(PATHGit,'binarizer.joblib'))


def text_cleaning(text):
    """
    Format the input text with use embedding
    """
    use_embedded_text = USE_model([text])
    return use_embedded_text

#prediction endpoint
@app.get("/predict-topics")
def predict_sentiment(text: str):
    """
    A simple function that receive a post content and predict the topics.
    :param review:
    :return: prediction, probabilities
    """
    # clean the review
    cleaned_text = text_cleaning(text)
    
    # perform prediction
    topics = model.predict(cleaned_text)
    
    tags =  binarizer.inverse_transform(topics)
    
    
    # result list initialization
    tag_list = []
 
    for tag in tags:
        for x in tag:
            tag_list.append(x)
    
    tag_dictionary = { "tags" : tag_list }

  
    
    return tag_dictionary