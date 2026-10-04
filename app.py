from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import numpy as np
from typing import Annotated, Literal

model = joblib.load('house_model.pkl')


app=FastAPI()

class houseinput(BaseModel):
    area:Annotated[float, Field(..., gt=0, description='area of the house in sqft')]
    bedrooms: Annotated[int, Field(..., gt=0, description='no. of bedrooms in the house')]
    bathrooms:Annotated[int,Field(..., gt=0, description='no. of bathrooms in the house')]
    stories:Annotated[int,Field(..., description='no. of stories in thehouse')]
    parking:Annotated[int,Field(..., description='no. of parkings available')]
    mainroad:Annotated[bool,Field(..., description='is the house on mainroad?')]
    furnishingstatus:Annotated[Literal['furnished','semi-furnished','unfurnished'], Field(..., description='furnishing status of the house')]

@app.get('/')
def home():
    return{'message':'house price prediction API'}

@app.post('/predict')
def predict(data:houseinput):
    
    mainroad = 1 if data.mainroad else 0

    furnishing_map = {
        'furnished': 0,
        'semi-furnished': 1,
        'unfurnished': 2
    }

    furnishing_encoded = furnishing_map[data.furnishingstatus]
    
    features = np.array([[
        data.area,
        data.bedrooms,
        data.bathrooms,
        data.stories,
        data.parking,
        mainroad,
        furnishing_encoded
    ]])

    prediction = model.predict(features)[0]


    if prediction < 4000000:
        category='low range'
    elif prediction < 8000000:
        category='mid range'
    else:
        category='high range'


    return {
        'predicted_price':  round(float(prediction),2),
        'predicted_category': category
    }
