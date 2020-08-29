import sklearn
from sklearn.linear_model import LogisticRegression
class MyLogisticRegression:
    def __init__(self,X_train,X_test,y_test,y_train):
        super().__init__()

    def fit(self,X,y):
        model = LogisticRegression()
        model.fit(X,y)

