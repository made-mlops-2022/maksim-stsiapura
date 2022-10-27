from models.log_reg import LogReg
from models.decision_tree import DecisionTree

import pickle
from enum import Enum
import pandas as pd


class Model(Enum):
    LOG_REG = 1
    DECISION_TREE = 2


def fit(model: Model, X_train, y_train, model_path):
    if model == Model.LOG_REG:
        clf = LogReg()
    elif model == Model.DECISION_TREE:
        clf = DecisionTree()
    clf.fit_and_save(X_train, y_train, model_path)


def predict(model_path, X_test, path_to_output="data/y_pred.csv"):
    with open(model_path, "rb") as fin:
        model = pickle.load(fin)
    y_pred = model.predict(X_test)
    pd.DataFrame(y_pred).to_csv(path_to_output, index=False)
