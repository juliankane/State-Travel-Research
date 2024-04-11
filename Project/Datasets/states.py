import pandas as pd
import os
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PER_CAPITA_FEATS = ['Number of Trips 100-250', 'Number of Trips 250-500', 'Number of Trips >=500', 'Electric (EV)', 'Hybrid Electric (HEV)', 'Gasoline', 'Diesel', "Total population in poverty status"]


@ staticmethod
def load_state_data(type = "", droplist = [], per_capita = True):
    if os.path.exists(f"states_aggregated_{type}.csv"):

        data = pd.read_csv(f"states_aggregated_{type}.csv")
        data.index = data['States']
        data.drop(columns='States', inplace=True)
        
        if per_capita:
            data = data.assign(**{col: data[col] / data['Total population'] for col in PER_CAPITA_FEATS})
        

        for drop in droplist:
            data.drop(columns=drop, inplace=True)



        return data
    else:
        raise FileNotFoundError