from typing import Optional
from fastapi import Depends, FastAPI
from pydantic import BaseModel
import pickle
import preprocessing
from enum import Enum

app = FastAPI()

class Sentiment(Enum):
    POSITIVE = 1
    NEGATIVE = 0

class Review(BaseModel):
    text: str
    reviewerID: Optional[str] = None
    productID: Optional[str] = None
    sentiment: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "text": "This was a great purchase, extremely useful!",
                "reviewerID": "A1VU337W6PKAR3",
                "productID": "B00K0TIC56"
            }
        }

def load_model():
    try:
      print ('Calling Depends Function')
      global prediction_model, vectorizer
      prediction_model = pickle.load(open('models/sentiment_classification.pickle','rb'))
      vectorizer = pickle.load(open('models/sentiment_vectorizer.pickle','rb'))
      print ('Models have been loaded')
    except Exception as e:
      raise ValueError('No model here')

@app.post("/api/v1/sentiment", response_model=Review)
def predict(review: Review, model = Depends(load_model())):
    text_clean = preprocessing.clean(review.text)
    text_tfidf = vectorizer.transform([text_clean])
    sentiment = prediction_model.predict(text_tfidf)
    review.sentiment = Sentiment(sentiment.item()).name
    return review
