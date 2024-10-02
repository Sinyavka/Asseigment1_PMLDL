import streamlit as st
import requests

st.title("Wine Quality Prediction App")

alcohol = st.number_input("Alcohol", value=12.0)
malic_acid = st.number_input("Malic Acid", value=1.0)
ash = st.number_input("Ash", value=2.0)
alcalinity_of_ash = st.number_input("Alcalinity of Ash", value=15.0)
magnesium = st.number_input("Magnesium", value=90.0)
total_phenols = st.number_input("Total Phenols", value=2.5)
flavanoids = st.number_input("Flavanoids", value=2.0)
nonflavanoid_phenols = st.number_input("Nonflavanoid Phenols", value=0.3)
proanthocyanins = st.number_input("Proanthocyanins", value=1.5)
color_intensity = st.number_input("Color Intensity", value=5.0)
hue = st.number_input("Hue", value=1.0)
od280_od315 = st.number_input("OD280/OD315", value=3.0)
proline = st.number_input("Proline", value=500.0)

if st.button("Predict"):
    payload = {
        "alcohol": alcohol,
        "malic_acid": malic_acid,
        "ash": ash,
        "alcalinity_of_ash": alcalinity_of_ash,
        "magnesium": magnesium,
        "total_phenols": total_phenols,
        "flavanoids": flavanoids,
        "nonflavanoid_phenols": nonflavanoid_phenols,
        "proanthocyanins": proanthocyanins,
        "color_intensity": color_intensity,
        "hue": hue,
        "od280_od315": od280_od315,
        "proline": proline
    }
    response = requests.post("http://api:8000/predict", json=payload)
    prediction = response.json().get("prediction")
    
    st.write(f"Prediction: {prediction}")
