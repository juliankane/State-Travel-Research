import numpy as np
import pandas as pd
from datetime import datetime
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

date = datetime.now().strftime('%S')

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
       'Colorado', 'Connecticut', 'Delaware', 'District of Columbia',
       'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
       'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts',
       'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
       'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
       'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
       'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
       'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
       'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

postal_codes_with_states = {'AL': 'Alabama','AK': 'Alaska','AZ': 'Arizona','AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'DC': 'District of Columbia',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming'
}


def aggregate_to_main(name, data = None):
    
    states_aggregated_source = pd.read_csv('states_aggregated_source.csv')
    states_aggregated_source.index = states_aggregated_source['States']
    states_aggregated_source.drop(columns='States', inplace=True)

    data = pd.read_csv(f'{name}.csv')
    data.index = data['States']
    data.drop(columns='States',inplace=True)
    new_data = states_aggregated_source.join(data, how='outer')

    new_data.replace(',','', regex=True)
    new_data = new_data.apply(pd.to_numeric, errors="coerce")
    new_data.to_csv(f'{date}states_aggregated_source.csv')

def no_age(data):
    drop_strings = ["years", "Male", "Female"]
    drop_from_strings(data, drop_strings)
    data.to_csv("states_aggregated_noage.csv")
    pass

def no_sex(data):
    drop_strings = ["Male", "Female"]
    drop_from_strings(data, drop_strings)
    data.to_csv("states_aggregated_nosex.csv")
    pass

def no_agesex(data):
    drop_strings = ["sex", "Male", "Female"]
    drop_from_strings(data, drop_strings)
    data.to_csv("states_aggregated_noagesex.csv")
    pass


def drop_from_strings(data, drop_strings):
    for col in data.columns:
        if any(string in col for string in drop_strings):
            data.drop(col, inplace=True, axis=1)
    return

def create_off_data(type = 'all'):
    states_aggregated_source = pd.read_csv("states_aggregated_source.csv")
    states_aggregated_source.index = states_aggregated_source['States']
    states_aggregated_source.drop(columns='States', inplace=True)

    no_age(states_aggregated_source)
    no_sex(states_aggregated_source)
    no_agesex(states_aggregated_source)


def adjust_source():
    states_aggregated_source = pd.read_csv('states_aggregated_source.csv')
    states_aggregated_source.index = states_aggregated_source['States']
    states_aggregated_source.drop(columns='States', inplace=True)

    states_aggregated_source.replace(',','', regex=True, inplace=True)
    new_data = states_aggregated_source.apply(pd.to_numeric, errors="coerce")
    new_data.to_csv(f'{date}states_aggregated_source.csv')


#adjust_source()
create_off_data()








# for key, value  in data_features_ready.items():
#      final_aggregate_test(value, key, to_csv= False)

# _drop_extra = pd.read_csv("C:/Users/Julia/OneDrive/Documents/GitHub/BigDataProject/aggregate/states_aggregated_source.csv")

# final_aggregate_test(_drop_extra, "no pop")


# _drop_extra = _drop_extra.replace(',','', regex=True).astype(float)

# _drop_extra.to_csv("states_aggregated_noAgeSex2.csv")


# trips = pd.read_csv("trips.csv").dropna()
# print(trips)



# print(trips)
# trips.index = trips['State Postal Code']

# trips.drop(columns=['Level', 'Month', 'Date', 'State Postal Code'], inplace=True)


# print(trips)
# trips = trips.replace(',','', regex=True).astype(float)

# #trips = trips.groupby("State Postal Code", as_index=True)#[["Number of Trips 100-250", "Number of Trips 250-500", 'Number of Trips >=500']].agg("sum")
# trips = trips.groupby("State Postal Code").sum()
# print(trips)

# index = trips.index
# new_index = []
# for i in index:
#     new_index.append(postal_codes_with_states[i])

# trips.index = new_index

    














