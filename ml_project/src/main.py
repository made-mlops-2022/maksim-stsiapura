from src.models.fit_predict import Model, fit, predict
from src.logger.base_logger import logger
from src.enities.fit_params import read_fit_params

import argparse
import pandas as pd

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--fit', action='store_true')
    parser.add_argument('--config', required=False)
    parser.add_argument('--predict', action='store_true')
    parser.add_argument("--X_train", default="data/X_train.csv")
    parser.add_argument("--y_train", default="data/y_train.csv")
    parser.add_argument("--model_path", default="models/model.sav")
    parser.add_argument("--X_test", default="data/X_test.csv")
    parser.add_argument("--y_test", default="data/y_test.csv")
    args = parser.parse_args()

    try:
        if args.fit:
            logger.info("fit model")
            if args.config:
                logger.info("params will be taken from config")
                fit_params = read_fit_params(args.config)

                model_type = Model.NONE
                if fit_params.model_type == "LogReg":
                    model_type = Model.LOG_REG
                elif fit_params.model_type == "DecisionTree":
                    model_type = Model.DECISION_TREE

                fit(model_type,
                    pd.read_csv(fit_params.x_train_path),
                    pd.read_csv(fit_params.y_train_path).condition,
                    fit_params.output_model_path)
            else:
                fit(Model.LOG_REG,
                    pd.read_csv(args.X_train),
                    pd.read_csv(args.y_train).condition,
                    args.model_path)

        if args.predict:
            logger.info("predict data")
            predict(args.model_path,
                    pd.read_csv(args.X_test),
                    args.y_test)

    except FileNotFoundError as err:
        logger.error("Passed invalid path: %s", err)
