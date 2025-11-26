import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

df = pd.read_csv("C:\\Users\\mailt\\Downloads\\Crop_recommendation.csv")

X = df[["ph", "humidity", "rainfall", "temperature", "N", "P", "K"]]
y = df["label"]

le = LabelEncoder()
y_encoded = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42) 

model = KNeighborsClassifier(n_neighbors=7)
model.fit(X_train, y_train)
pred = model.predict(X_test)

with open("model\\crop_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model\\crop_encoder.pkl", "wb") as f:
    pickle.dump(le, f)