import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

df = pd.read_csv("C:\\Users\\mailt\\Downloads\\Crop_recommendation.csv")

soil_map = {
    "grapes" : "sandy loam", 
    "bajra" : "sandy loam", 
    "cabbage" : "clay loam",
    "cauliflower" : "loam", 
    "cotton" : "black soil", 
    "jowar" : "loam", 
    "maize" : "alluvial soil", 
    "onion" : "sandy loam", 
    "pomegranate" : "light black soil", 
    "potato" : "sandy loam",
    "rice" : "clayey soil", 
    "soyabean" : "black soil", 
    "sugarcane" : "alluvial soil", 
    "tomato" : "sandy loam",
    "wheat" : "loamy soil"
}

df["soil_type"] = df["label"].map(soil_map)
df = df.dropna(subset=["soil_type"])


X = df[["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]]
y = df["soil_type"]

le = LabelEncoder()
y_encoded = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Soil Classes:", le.classes_)

with open("model\\soil_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model\\soil_encoder.pkl", "wb") as f:
    pickle.dump(le, f)