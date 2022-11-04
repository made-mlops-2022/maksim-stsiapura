from src.models.fit_predict import Model, fit, predict
from src.data.split_train_test import split_train_test

import unittest
import pandas as pd
import os
import subprocess as sp
from sklearn.metrics import accuracy_score

ROW_DATA_PATH = "data/heart_cleveland_upload.csv"
X_TRAIN_PATH = "data/X_train.csv"
Y_TRAIN_PATH = "data/y_train.csv"
X_TEST_PATH = "data/X_test.csv"
Y_TEST_PATH = "data/y_test.csv"
Y_PRED_PATH = "data/y_pred.csv"
LOG_REG_MODEL_PATH = "models/log_reg.sav"
DECISION_TREE_MODEL_PATH = "models/decision_tree.sav"

MODELS = [Model.LOG_REG, Model.DECISION_TREE]

MODEL_TO_PATH = {
    Model.LOG_REG: LOG_REG_MODEL_PATH,
    Model.DECISION_TREE: DECISION_TREE_MODEL_PATH
}

MODEL_TO_SCORE = {
    Model.LOG_REG: 0.85,
    Model.DECISION_TREE: 0.65
}


class TestData(unittest.TestCase):
    def test_data(self):
        sp.call("python src/data/download_dataset.py", shell=True)
        self.assertTrue(os.path.exists(ROW_DATA_PATH))

        X_train, X_test, y_train, y_test = split_train_test(ROW_DATA_PATH)

        X_train.to_csv(X_TRAIN_PATH)
        self.assertTrue(os.path.exists(X_TRAIN_PATH))

        y_train.to_csv(Y_TRAIN_PATH)
        self.assertTrue(os.path.exists(Y_TRAIN_PATH))

        X_test.to_csv(X_TEST_PATH)
        self.assertTrue(os.path.exists(X_TEST_PATH))

        y_test.to_csv(Y_TEST_PATH)
        self.assertTrue(os.path.exists(Y_TEST_PATH))


class TestFit(unittest.TestCase):
    def test_fit(self):
        for model in MODELS:
            fit(model,
                pd.read_csv(X_TRAIN_PATH),
                pd.read_csv(Y_TRAIN_PATH).condition,
                MODEL_TO_PATH[model])
            self.assertTrue(os.path.exists(MODEL_TO_PATH[model]))


class TestPredict(unittest.TestCase):
    def test_predict(self):
        for model in MODELS:
            predict(MODEL_TO_PATH[model],
                    pd.read_csv(X_TEST_PATH),
                    Y_PRED_PATH)
            self.assertTrue(os.path.exists(Y_PRED_PATH))

            y_test = pd.read_csv(Y_TEST_PATH)
            y_pred = pd.read_csv(Y_PRED_PATH)
            self.assertGreater(accuracy_score(y_test.condition,
                                              y_pred), MODEL_TO_SCORE[model])


if __name__ == "__main__":
    unittest.main()
