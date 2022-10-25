import os
import json

DATASET_URL = "https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci"
DATA_PATH = "data/"
KAGGLE_CREDS_PATH = "credentials/kaggle.json"


with open(KAGGLE_CREDS_PATH) as fin:
    kaggle_creds = json.loads(fin.read())
os.environ["KAGGLE_USERNAME"] = kaggle_creds["username"]
os.environ["KAGGLE_KEY"] = kaggle_creds["key"]
from kaggle.api.kaggle_api_extended import KaggleApi

if __name__ == "__main__":
    api = KaggleApi()
    api.authenticate()
    
    os.makedirs(DATA_PATH, exist_ok=True)
    api.dataset_download_files(dataset="cherngs/heart-disease-cleveland-uci", path=DATA_PATH, unzip=True)
