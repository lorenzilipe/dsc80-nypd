# functions.py

from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd

class BetterLabelEncoder(BaseEstimator, TransformerMixin):

    def __init__(self):
        pass

    def fit(self, X, y=None):
        self.classes_ = {k : v for v, k in enumerate(np.unique(X))}
        return self

    def fit_transform(self, X, y=None):
        self.classes_ = {k : v for v, k in enumerate(np.unique(X))}

        return self.transform(X, y)

    def transform(self, X, y=None):
        try:
            getattr(self, "classes_")
        except AttributeError:
            raise RuntimeError("You must fit the transformer before tranforming the data!")

        def replace_value_handle_unknown(x):
            try:
                return self.classes_[x]
            except:
                return -1

        encoded = np.array(list(map(replace_value_handle_unknown, X))).reshape(-1, 1)

        return pd.DataFrame(encoded)