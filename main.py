from fastapi import FastAPI
import json

app = FastAPI()


# Loading the JSON file of patient
def load_data():
    with open("patient.json","r") as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {'message':'Patient Management System'}

@app.get("/doc")
def hello():
    return {'message':'A fully funcitonal patient management system.'}


@app.get("/view")
def view():
    data = load_data()
    
    return data