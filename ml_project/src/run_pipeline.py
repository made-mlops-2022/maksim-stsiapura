from models.fit_predict import Model, fit, predict

import logging
import argparse
import pandas as pd

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--fit', action='store_true')
    parser.add_argument('--predict', action='store_true')
    parser.add_argument("--X_train", default="data/X_train.csv")
    parser.add_argument("--y_train", default="data/y_train.csv")
    parser.add_argument("--model_path", default="models/model.sav")
    parser.add_argument("--X_test", default="data/X_test.csv")
    parser.add_argument("--y_test", default="data/y_test.csv")
    args = parser.parse_args()

    logging.info("pipeline started")

    if args.fit or True:
        fit(Model.LOG_REG,
            pd.read_csv(args.X_train),
            pd.read_csv(args.y_train).condition,
            args.model_path)

    if args.predict:
        predict(args.model_path, pd.read_csv(args.X_test), args.y_test)
