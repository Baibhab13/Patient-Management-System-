from fastapi import FastAPI, Path, HTTPException, Query
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

@app.get('/patient/{patient_id}')
def view_patient(patient_id:str = Path(..., description='Id of the patient in DB', example='P001')):
    #load the data
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code = 404, detail = 'Patient not found')

@app.get('/sort')
def sort_patient(sort_by: str = Query(..., description = 'Sort the patient on the basis of weight, height or bmi'),
                 order: str = Query('asc', description='order by ascending order until mentioned')):

    valid_fields = ['weight', 'height', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail= f'Bad Request: Invalid field Select from {valid_fields}')

    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail= f'Invalid order select in between asc and desc')

    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x:x.get('sort_by', 0), reverse = sort_order)

    return sorted_data,