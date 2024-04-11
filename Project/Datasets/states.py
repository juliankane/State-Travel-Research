import pandas as pd
import os
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


@ staticmethod
def load_state_data(type = ""):
    if os.path.exists(f"states_aggregated_{type}.csv"):
        data = pd.read_csv(f"states_aggregated_{type}.csv")
        data.index = data['States']
        data.drop(columns='States', inplace=True)
        
        return data
    else:
        raise FileNotFoundError
    
    return False