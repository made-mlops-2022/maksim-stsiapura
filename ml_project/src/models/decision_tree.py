from sklearn.tree import DecisionTreeClassifier
import pickle


class DecisionTree:
    def __init__(self):
        self.__model = DecisionTreeClassifier()

    def fit_and_save(self, X_train, y_train, model_path):
        self.__model.fit(X_train, y_train)

        with open(model_path, 'wb') as fout:
            pickle.dump(self.__model, fout)
