from fastapi import FastAPI
import joblib
from pydantic import BaseModel

model = joblib.load('/app/models/trained_model.pkl')

app = FastAPI()

class WineFeatures(BaseModel):
    alcohol: float
    malic_acid: float
    ash: float
    alcalinity_of_ash: float
    magnesium: float
    total_phenols: float
    flavanoids: float
    nonflavanoid_phenols: float
    proanthocyanins: float
    color_intensity: float
    hue: float
    od280_od315: float
    proline: float

@app.post("/predict")
def predict(features: WineFeatures):
    data = [[
        features.alcohol, features.malic_acid, features.ash, features.alcalinity_of_ash,
        features.magnesium, features.total_phenols, features.flavanoids, features.nonflavanoid_phenols,
        features.proanthocyanins, features.color_intensity, features.hue, features.od280_od315, features.proline
    ]]
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}
