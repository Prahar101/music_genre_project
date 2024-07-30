from fastapi import FastAPI, UploadFile
from keras.models import load_model
import librosa
import uvicorn
import pickle
import numpy as np
import tempfile

app = FastAPI()
model = load_model('model.h5')

with open('le.pkl', "rb") as f:
    le = pickle.load(f)

def extract_features(file_path):
    audio, sample_rate = librosa.load(file_path, sr=None)
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs = np.mean(mfccs.T, axis=0)
    return mfccs

@app.post("/predict")
async def predict(file: UploadFile):
    contents = await file.read()
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(contents)
        tmp_path = tmp.name
    
    mfccs = extract_features(tmp_path)
    mfccs = mfccs.reshape(1, 40, 1, 1)  # Reshape to match model input shape
    result = model.predict(mfccs)
    y_pred = np.argmax(result, axis=1)
    ans = le.inverse_transform(y_pred)
    return {'prediction': ans[0]}

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
