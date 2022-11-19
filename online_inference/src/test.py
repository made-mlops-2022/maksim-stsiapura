import json
import pytest
from fastapi.testclient import TestClient
from app import app, load_model

client = TestClient(app)


@pytest.fixture(scope="session", autouse=True)
def initialize_model():
    load_model()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.text == "true"


def test_predict():
    response = client.post("/predict",
                           json.dumps({
                               "age": 44,
                               "sex": 0,
                               "cp": 2,
                               "trestbps": 118,
                               "chol": 242,
                               "fbs": 0,
                               "restecg": 0,
                               "thalach": 149,
                               "exang": 0,
                               "oldpeak": 0.3,
                               "slope": 1,
                               "ca": 1,
                               "thal": 0
                           }))
    assert response.status_code == 200
    assert response.json() == True


def test_missing_fields():
    response = client.post("/predict",
                           json.dumps({
                               "age": 44,
                               "sex": 0,
                               "cp": 2,
                               "trestbps": 118,
                               "fbs": 0,
                               "restecg": 0,
                               "thalach": 149,
                               "exang": 0,
                               "oldpeak": 0.3,
                               "slope": 1,
                               "ca": 1
                           }))
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "field required"


def test_categorical_fields():
    response = client.post("/predict",
                           json.dumps({
                               "age": 44,
                               "sex": 3,
                               "cp": 2,
                               "trestbps": 118,
                               "chol": 242,
                               "fbs": 0,
                               "restecg": 0,
                               "thalach": 149,
                               "exang": 0,
                               "oldpeak": 0.3,
                               "slope": 1,
                               "ca": 1,
                               "thal": 0
                           }))
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == \
        "unexpected value; permitted: 0, 1"


def test_numerical_fields():
    response = client.post("/predict",
                           json.dumps({
                               "age": "",
                               "sex": 0,
                               "cp": 2,
                               "trestbps": 118,
                               "chol": 242,
                               "fbs": 0,
                               "restecg": 0,
                               "thalach": 149,
                               "exang": 0,
                               "oldpeak": 0.3,
                               "slope": 1,
                               "ca": 1,
                               "thal": 0
                           }))
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == \
        "value is not a valid float"
