from patient import Patient

import os
import pickle
import uvicorn
import pandas as pd
from fastapi import FastAPI
from fastapi_health import health

app = FastAPI()
model = None


@app.on_event("startup")
def load_model():
    with open(os.getenv("PATH_TO_MODEL"), "rb") as f:
        global model
        model = pickle.load(f)


@app.get("/")
async def root():
    return "Hello!"


@app.post("/predict")
async def predict(data: Patient):
    X = pd.DataFrame([data.dict()])
    y = model.predict(X)
    return True if not y[0] else False


def check_model():
    return model is not None


async def handle_success(**kwargs):
    return True


async def handle_failure(**kwargs):
    return False


app.add_api_route("/health", health([check_model],
                                    success_handler=handle_success,
                                    failure_handler=handle_failure))

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000)
