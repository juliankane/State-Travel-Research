import numpy as np
import pandas as pd
from datetime import datetime
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
date = datetime.now().strftime('%S')



'''
All of these are called from TravelDistance
'''
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
def adjust_source_datatypes(dataset, index = "State"):
    dataset.index = dataset[index]
    dataset.drop(columns=index, inplace=True)

    dataset.replace(',','', regex=True, inplace=True)
    adjusted = dataset.apply(pd.to_numeric, errors="coerce")
    return adjusted




##### playground



















