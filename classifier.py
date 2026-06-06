
import joblib

model = joblib.load("models/model.pkl")

def classify_document(text):

    prediction = model.predict([text])[0]  #wny [text]=single sentence bhi list me leta hai

    confidence = max(model.predict_proba([text])[0])  #Prediction kitna accurate/confident hai.

    return prediction, round(float(confidence), 2)
