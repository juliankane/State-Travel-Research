import numpy as np
import pandas as pd
from datetime import datetime
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
date = datetime.now().strftime('%S')



'''
All of these are called from TravelDistance
'''

northeast_states = ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont', 'New Jersey', 'New York', 'Pennsylvania']
southeast_states = ['Alabama', 'Arkansas', 'Delaware', 'Florida', 'Georgia', 'Kentucky', 'Louisiana', 'Maryland', 'Mississippi', 'North Carolina', 'Oklahoma', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'West Virginia']
south_states = ['Arizona', 'New Mexico', 'Texas', 'Oklahoma', 'Arkansas', 'Louisiana', 'Mississippi', 'Alabama', 'Florida', 'Georgia', 'South Carolina', 'North Carolina', 'Tennessee']
midwest_states = ['Illinois', 'Indiana', 'Iowa', 'Kansas', 'Michigan', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'Ohio', 'South Dakota', 'Wisconsin']
west_states = ['Alaska', 'California', 'Colorado', 'Hawaii', 'Idaho', 'Montana', 'Nevada', 'Oregon', 'Utah', 'Washington', 'Wyoming']


regions = {
    'Northeast': northeast_states,
    'Southeast': southeast_states,
    'South': south_states,
    'Midwest': midwest_states,
    'West': west_states
}



northeast_abbreviations = ['CT', 'ME', 'MA', 'NH', 'RI', 'VT', 'NJ', 'NY', 'PA']
southeast_abbreviations = ['AL', 'AR', 'DE', 'FL', 'GA', 'KY', 'LA', 'MD', 'MS', 'NC', 'OK', 'SC', 'TN', 'TX', 'VA', 'WV']
south_abbreviations = ['AZ', 'NM', 'TX', 'OK', 'AR', 'LA', 'MS', 'AL', 'FL', 'GA', 'SC', 'NC', 'TN']
midwest_abbreviations = ['IL', 'IN', 'IA', 'KS', 'MI', 'MN', 'MO', 'NE', 'ND', 'OH', 'SD', 'WI']
west_abbreviations = ['AK', 'CA', 'CO', 'HI', 'ID', 'MT', 'NV', 'OR', 'UT', 'WA', 'WY']

regions_abrv = {
    'Northeast': northeast_abbreviations,
    'Southeast': southeast_abbreviations,
    'South': south_abbreviations,
    'Midwest': midwest_abbreviations,
    'West': west_abbreviations


}

# don't include these in datasets
DROP_INDEX = ['United States', 'District of Columbia', 'Puerto Rico']

# dict to swap labels if needed
STATE_DICT = {'AL': 'Alabama','AK': 'Alaska','AZ': 'Arizona','AR': 'Arkansas', 'CA': 'California',
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

# drop stuff from biggly datasets
def drop_from_strings(data, drop_strings):
    for col in data.columns:
        if any(string in col for string in drop_strings):
            data.drop(col, inplace=True, axis=1)
    return

# prepare the index and datatypes of datasets
def adjust_source_datatypes(dataset, index = "") -> pd.DataFrame:
    
    dataset.index = dataset[index]
    dataset.drop(columns=index, inplace=True)

    dataset.replace(',','', regex=True, inplace=True)
    adjusted = dataset.apply(pd.to_numeric, errors="coerce")
    return adjusted




##### playground


















