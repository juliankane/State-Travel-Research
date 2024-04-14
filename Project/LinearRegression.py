from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score





class LR_Model:
    def __init__(self, data):
        '''
            Processs data with optimal parameters
                - data - Dataframe already loaded into data
        '''
        self.data = data
        print(self.data)
        
        self.regression_count = 0
        self.past_regression= { 1:     
                {

                }
        }
        
    def train_do_analysis(self, predictor:str, trainsize:float, state_size:int, predict_idx:str):
        X = self.data.drop(columns=predictor, axis=1)
        y = self.data[predictor]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=trainsize, random_state=state_size)

        lr = LinearRegression()
        lr.fit(X_train, y_train)
        lr.predict(X_test)

        y_pred = lr.predict(X_test)

        # print Coefficients slope & slope intercept
        print("LR beta/slope Coefficient:                 ", lr.coef_)
        print("LR alpha/slope intercept Coefficient       ", lr.intercept_)
        print(f"Root Mean Squared Error (RMSE):           {np.sqrt(mean_squared_error(y_test, y_pred))}")
        print("\n")



        actual_df = self.data[predict_idx]
        prediction_df = self.data.drop(predictor, axis=1, inplace=False)
        prediction_result = lr.predict(prediction_df)
        
        print(f"Predicted {predictor}     :     {prediction_result[0]}")
        print(f"Actual {predictor}        :     {actual_df.iloc[0]}")
        print(f"Desperator is         :     {abs(prediction_result[0] - actual_df.iloc[0])}")
        print("\n\n")
        pass




    def do_regression(self, predictor, **kwargs) -> None:
        train_size = kwargs.get('train_size', 0.2)
        state_size = kwargs.get('state_size',100)
        predict_idx = kwargs.get('predict_idx', 10)
        self.regression_count += 1
        self.past_regression = {self.regression_count: {"Predicted Feature":predictor, "Training Size": train_size, "State Size": state_size, "Prediction Index": predict_idx}}
        self.train_do_analysis(predictor, train_size, state_size, predict_idx)

        print(f"Train on {train_size} ...")
        self.train_do_analysis(predictor, trainsize = train_size, state_size = state_size, predict_idx = predict_idx)
        pass

  

    def print_last_regression(self, index:int):

        print(self.past_regression[index])
        pass
            

    def save_results_to_json():
        pass
