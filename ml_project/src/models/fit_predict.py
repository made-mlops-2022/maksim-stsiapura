from logger.base_logger import logger
from models.log_reg import LogReg
from models.decision_tree import DecisionTree

import pickle
from enum import Enum
import pandas as pd


class Model(Enum):
    LOG_REG = 1
    DECISION_TREE = 2


def fit(model: Model, X_train, y_train, model_path):
    logger.debug("method fit called")
    if model == Model.LOG_REG:
        clf = LogReg()
        logger.debug("log reg model used")
    elif model == Model.DECISION_TREE:
        clf = DecisionTree()
        logger.debug("decision tree model used")
    clf.fit_and_save(X_train, y_train, model_path)
    logger.debug("model saved in %s", model_path)


def predict(model_path, X_test, path_to_output="data/y_pred.csv"):
    with open(model_path, "rb") as fin:
        model = pickle.load(fin)
        logger.debug("model loaded from %s", model_path)
    y_pred = model.predict(X_test)
    logger.debug("predict data generated")
    pd.DataFrame(y_pred).to_csv(path_to_output, index=False)
    logger.debug("predict data saved to %s", path_to_output)
