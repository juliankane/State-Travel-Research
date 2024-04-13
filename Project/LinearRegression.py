from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score





class LinearRegression:

    def __init__(self, **kwargs):
        '''
            Processs data with optimal parameters
                - data - Dataframe already loaded into data
                - prediction - feature to be to predicted

                Optional: 
                    - index to predict - now is given -> random index in the dataset
                    - train_size -   none is given defaults to 0.2
                    - state_size    -   data shuffle, defaults to 100
        '''
        self.data = kwargs.get('data', None)
        if self.data is None:
            raise TypeError    
        
        self.regression_count = 0
        self.past_regression= { 1:     
                {

                }
        }
        
def do_regression(self, predictor,  **kwargs):
    train_size = kwargs.get('train_size', 0.2)
    state_size = kwargs.get('state_size',100)
    predict_idx = kwargs.get('predict_idx', -1)
    self.regression_count += 1
    self.past_regression = {self.regression_count: {"Predicted Feature":predictor, "Training Size": train_size, "State Size": state_size, "Prediction Index": predict_idx}}
    self.train_do_analysis(predictor)

    print(f"Train on {train_size} ... \n")
    train_do_analysis(predictor, trainsize = train_size, state_size = state_size, predict_idx = predict_idx)
    pass

def train_do_analysis(self, predictor, trainsize:float, state_size:int, predict_idx:any):
    
    X = self.data.drop(predictor, axis=1)
    y = self.data[predictor]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=trainsize, random_state=state_size)

    lr = LinearRegression()
    lr.predict(X_train, y_train)

    y_pred = lr.predict(X_test)

    # print Coefficients slope & slope intercept
    print("LR beta/slope Coefficient:                 ", lr.coef_)
    print("LR alpha/slope intercept Coefficient       ", lr.intercept_)

    # Root Mean Squared
    print(f"Root Mean Squared Error (RMSE):           {np.sqrt(mean_squared_error, y_test, y_pred)}\n\n")

    actual_df = pd.DataFrame(self.data.loc[predictor]).T
    prediction_df = actual_df.drop(predictor, axis=1, inplace=False)

    prediction_result = lr.predict(prediction_df)
    
    print(f"Predicted {predictor}  :     {prediction_result[predict_idx]}")
    print(f"Actual {predictor}    :     {actual_df[predictor].iloc[predict_idx]}")

    self.past_regression[self.regression_count]["Results"] = {"LR beta/slope Coefficient": lr.coef_,
                                                               "LR alpha/slope intercept Coefficient": lr.intercept_, 
                                                              "Root Mean Square RMSE" : np.sqrt(mean_squared_error, y_test, y_pred),
                                                              "Predicted feature": prediction_result[predict_idx],
                                                              "Actual feature": actual_df[predictor].iloc[predict_idx]
                                                              } 
    pass


def print_last_regression(self, index:int):

    print(self.past_regression[index])
    pass
        

def save_results_to_json():
    pass
