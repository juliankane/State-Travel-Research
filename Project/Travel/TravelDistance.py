import pandas as pd
import os
cwd = os.getcwd()
from Travel.aggregate import Aggregation # import functions from Aggregation
os.chdir(os.path.dirname(os.path.abspath(__file__)))



PER_CAPITA_FEATS = ["vehicles", "poverty", "age", "trips"] # add any per capita feature data here

'''
class to easily integrate new datasets into the mix for feature selection
usage:
    trave_data = TravelDistance()    # don't change any of the default parameters
    df = travel_data.feature_data(...)
'''
class TravelDistance: 
    def __init__(self, area = "State", year = '2022', distance_range = (0,)):

        area = "State" # ignore
        self.area = area # always state -------- include national/county later maybe
        self.year = year # always 2022  -------- hard to find a lot of matching data all for 2022
        self.trips_df = None 
        self.areas = ["State"] 


        # feature data included in Travel/Subsets
        self.feature_data = ["airports", "gdp", "household_income", 
                             "poverty", "vehicles", "personal_expenditures"]
        
        # trips_by_distance in trips_data.csv
        self.trips_distance = ['Trips <1', 'Trips 1-3', 'Trips 3-5', 'Trips 5-10', 'Trips 10-25', 'Trips 25-50', 'Trips 50-100', 'Trips 100-250', 'Trips 250-500', 'Trips >=500'] 


        # load travel data on __init__
        self.travel_data = self._loadTravelData(area, year, distance_range) 

    def _loadTravelData(self, area, year, distance):
        trav_df = pd.read_csv("trips_data.csv")

        # aggregate trips by year / location
        trav_df.index = trav_df['Date'].astype('str')
        trav_df.drop(columns="Date", inplace=True)
        trav_df_year = trav_df[trav_df.index.str.contains(year)]

        _unused = [location for location in self.areas if location != area]
        _unused.append("Date")
        
        if area in self.areas:
            trips_df_year = trav_df_year.groupby(area)[self.trips_distance].sum()
        else:
            raise ValueError
        
        # return
        self.trips_df = trips_df_year
    

    '''
    returns dataframe with feature data
    IF no arguments are given - load all feature data except 'age'
    
        
    # labels - "full" - state names, "abrv" -abbreviations 
    # locations - unused - always 'State' 

    # exclude - features to exclude
    # only - features to incllude
        # note: don't use both together
    
    # include_age - include age into analysis
         # note: you can use only = "age"  to just get the age 

    '''

    def load_feature_data(self, labels = "full", locations = [], exclude = [], only = [], include_age = False):
        if exclude and only:
            raise ValueError("These parameters should not be used together")
        
        # ignore
        if labels == "full":
            self.trips_df.index = self.trips_df.index.map(Aggregation.STATE_DICT)
        else:
            self.trips_df.index = self.trips_df.index.map(Aggregation.STATE_DICT)
        
        # to coerce parameters exclude & only into a list if only one feature was given
        def ceorce_list(input):
            if not isinstance(input, list):
                return [input]
            else:
                return input
            
        # prepare the datatypes and indices of each dataset being joined together
        def prepare(df, datatypes = True, labels = True):
            if datatypes:
                df = Aggregation.adjust_source_datatypes(df, index = "State")   
            if labels:
                drop_idx = locations + Aggregation.DROP_INDEX
                df.drop(index=drop_idx, inplace=True, errors='ignore')
                df.sort_index(inplace=True)
            return df
    
        # load population to divide any datasets that need to be per capita
        _population = pd.read_csv("population_totals.csv")
        pop = prepare(_population)


        # get selected data - defaults on ALL features except age
        selection = []
        if only:
            only = ceorce_list(only)
            selection.extend(only)
        elif exclude:
            exclude = ceorce_list(exclude)
            selection = [feature for feature in self.feature_data if feature not in exclude]
        else:
            selection = self.feature_data

        # age selected ----- check for 'only = "age"'
        if include_age and "age" not in selection:
            selection.append("age")

        # load and join datasets from /Subsets/.csv's
        for dataset in selection:
            if dataset in selection:
                feature_df = pd.read_csv(f'Subsets/{dataset}.csv')
                df = prepare(feature_df)

                if dataset in PER_CAPITA_FEATS:
                    df = df.assign(**{col: df[col] / pop[f"Pop. {self.year}"] for col in df.columns})
                self.trips_df = self.trips_df.join(df, how="outer")

        # prepare and return final set
        self.trips_df = prepare(self.trips_df, datatypes=False).dropna(axis=0)    
        return self.trips_df
    

    def get_features(self):
        return self.trips_distance

