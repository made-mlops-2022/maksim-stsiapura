import json
import requests
import pandas as pd
import gdown

REQUEST_URL = "http://127.0.0.1:5000/predict"

DATA_URL = "https://drive.google.com/uc?id=1b8tv5WYDxM9ovbjzL1OBoAfz6SZYKaMj"
DATA_PATH = "data/data.csv"

if __name__ == "__main__":
    gdown.download(DATA_URL, DATA_PATH, quiet=True)

    data = pd.read_csv(DATA_PATH)
    for record in data.to_dict(orient="records"):
        response = requests.post(REQUEST_URL, json.dumps(record))
        print(f"{response.status_code=}, {response.text=}")
