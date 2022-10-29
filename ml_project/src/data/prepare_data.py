from src.data.split_train_test import split_train_test

PATH_TO_DATA = "data/heart_cleveland_upload.csv"
PATH_TO_X_TRAIN = "data/X_train.csv"
PATH_TO_Y_TRAIN = "data/y_train.csv"
PATH_TO_X_TEST = "data/X_test.csv"

X_train, X_test, y_train, y_test = split_train_test(PATH_TO_DATA)
X_train.to_csv(PATH_TO_X_TRAIN)
y_train.to_csv(PATH_TO_Y_TRAIN)
X_test.to_csv(PATH_TO_X_TEST)
