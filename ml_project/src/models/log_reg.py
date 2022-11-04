from sklearn.linear_model import LogisticRegression
from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning
import pickle


class LogReg:
    def __init__(self):
        self.__model = LogisticRegression(solver='lbfgs', max_iter=500)

    @ignore_warnings(category=ConvergenceWarning)
    def fit_and_save(self, X_train, y_train, model_path):
        self.__model.fit(X_train, y_train)

        with open(model_path, 'wb') as fout:
            pickle.dump(self.__model, fout)
