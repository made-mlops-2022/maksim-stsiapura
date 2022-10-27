import pandas as pd
from sklearn.model_selection import train_test_split


def split_train_test(path_to_data="data/heart_cleveland_upload.csv",
                     test_size=0.2,
                     random_state=1):
    df = pd.read_csv(path_to_data)
    X = df.drop("condition", axis="columns")
    y = df.condition
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=test_size,
                                                        random_state=random_state)
    return X_train, X_test, y_train, y_test
