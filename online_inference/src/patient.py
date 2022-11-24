from typing import Literal
from pydantic import BaseModel, validator
from fastapi import HTTPException


class Patient(BaseModel):
    id: int = 0
    age: float
    sex: Literal[0, 1]
    cp: Literal[0, 1, 2, 3]
    trestbps: float
    chol: float
    fbs: Literal[0, 1]
    restecg: Literal[0, 1, 2]
    thalach: float
    exang: Literal[0, 1]
    oldpeak: float
    slope: Literal[0, 1, 2]
    ca: Literal[0, 1, 2, 3]
    thal: Literal[0, 1, 2]

    @validator("id")
    def id_validator(cls, v):
        if v < 0:
            raise HTTPException(
                status_code=400, detail="ID must not be negative")
        return v

    @validator("age")
    def age_validator(cls, v):
        if v < 0 or v > 150:
            raise HTTPException(
                status_code=400, detail="Age is out of human range")
        return v

    @validator("trestbps")
    def trestbps_validator(cls, v):
        if v < 0 or v > 250:
            raise HTTPException(
                status_code=400, detail="Resting blood is out of human range")
        return v

    @validator("chol")
    def chol_validator(cls, v):
        if v < 0 or v > 700:
            raise HTTPException(
                status_code=400, detail="Serum cholesterol is out of human range")
        return v

    @validator("thalach")
    def thalach_validator(cls, v):
        if v < 0 or v > 250:
            raise HTTPException(
                status_code=400, detail="Maximum heart rate achieved is out of human range")
        return v

    @validator("oldpeak")
    def oldpeak_validator(cls, v):
        if v < 0 or v > 8:
            raise HTTPException(
                status_code=400, detail="ST depression induced by exercise relative to rest is out of human range")
        return v
