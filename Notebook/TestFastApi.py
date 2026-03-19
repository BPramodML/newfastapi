from fastapi import FastAPI
from uvicorn import run
import pickle

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
    
@app.get("/pramod")
def read_root():
    return {"welcome pramod"}

@app.get("/name/{name}")
def read_name(name: str):
    return f"welcome to the workd of FastAPI {name}"

pickle_in = open("model.pkl", "rb")
model = pickle.load(pickle_in)

@app.get("/predict/{experience}")
def predict_salary(experience: float):
    prediction = model.predict([[experience]])
    return f"The predicted salary for {experience} years of experience is {prediction[0]}"

if __name__ == "__main__":
    run(app, host="127.0.0.1", port=8000)

