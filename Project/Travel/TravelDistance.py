import pandas as pd
import os
cwd = os.getcwd()
from Travel.aggregate import Aggregation # import functions from Aggregation
os.chdir(os.path.dirname(os.path.abspath(__file__)))




PER_CAPITA_FEATS = ["vehicles", "poverty", "age", "trips", "airports"] # add any per capita feature data here

'''
class to easily integrate new datasets into the mix for feature selection
usage:
    trave_data = TravelDistance()    # don't change any of the default parameters
    df = travel_data.feature_data(...)
'''
class TravelDistance: 
    def __init__(self, area = "State", year = '2022', distance_range = (0,)):

        self.area = area # state/regional
        self.year = year # always 2022 
        self.trips_df = None 
        self.areas = ["State", "Region"] 
        self.regions = Aggregation.regions_abrv

        # feature data included in Travel/Subsets
        self.feature_data = ["airports", "gdp", "household_income", 
                             "poverty", "vehicles", "personal_expenditures"]
        
        # distance of trips
        self.trips_distance = ['Trips <1', 'Trips 1-3', 'Trips 3-5', 'Trips 5-10', 'Trips 10-25', 'Trips 25-50', 'Trips 50-100', 'Trips 100-250', 'Trips 250-500', 'Trips >=500'] 

        # ld travel data
        self.travel_data = self._loadTravelData(distance_range) 


    def _loadTravelData(self, distance):
        trips = pd.read_csv("trips_data.csv")

        # aggregate trips by year / location
        trips.index = trips['Date'].astype('str')
        trips.drop(columns="Date", inplace=True)
        trips = trips[trips.index.str.contains(self.year)]

      

        if self.area in self.areas:
            if self.area == "Region":
                trips['Region'] = trips['State'].map({state: region for region, states in self.regions.items() for state in states})
                trips = trips.groupby('Region')[self.trips_distance].sum()
            elif self.area == "State":
                trips = trips.groupby(self.area)[self.trips_distance].sum()
        else:
            raise ValueError
        trips.sort_index(inplace=True)
        self.trips_df = trips
    

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
    def load_feature_data(self, labels = "full", locations = [], exclude = [], only = [], include_age = False) -> pd.DataFrame:
        if exclude and only:
            raise ValueError("These parameters should not be used together")
        

        # ignore
        # if labels == "full":
        #     self.trips_df.index = self.trips_df.index.map(Aggregation.STATE_DICT)
        # else:
        #     self.trips_df.index = self.trips_df.index.map(Aggregation.STATE_DICT)
        # to coerce parameters exclude & only into a list if only one feature was given

        def ceorce_list(input): # inputs to this function were just a string
            if not isinstance(input, list):
                return [input]
            else:
                return input
    
        def prepare_datatypes(df, idx = self.area): # prepare datatypes
            if idx == "State":
                df = Aggregation.adjust_source_datatypes(df, index = idx)   
                return df
            else:
                df.reset_index(drop=True,inplace=True)
                df['Region'] = df['State'].map({state: region for region, states in Aggregation.regions.items() for state in states})
                df = Aggregation.adjust_source_datatypes(df, index=self.area).dropna(how='all',axis=1)
                regional = df.groupby('Region')[df.columns].sum()
                return regional
            
        def drop_excess_labels(df): # drop excess labels, e.g. District of Colombia, Puerto rico
            drop_idx = locations + Aggregation.DROP_INDEX
            df.drop(index=drop_idx, inplace=True, errors='ignore')
            df.sort_index(inplace=True)
            return df

        def adjust_per_capita(df, population, idx = self.area, year = self.year): # adjust per capita
            return df.assign(**{col: df[col] / population[f"Pop. {self.year}"] for col in df.columns})
        
        

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
        if include_age and "age" not in selection:
            selection.append("age")



         # load population totals
        _population = pd.read_csv("population_totals.csv")
        pop = prepare_datatypes(_population, self.area)
        pop = drop_excess_labels(pop)
     
        self.trips_df = adjust_per_capita(self.trips_df, pop)



        # load and join datasets from /Subsets/.csv's
        for dataset in selection:
            if dataset in selection:
                feature_df = pd.read_csv(f'Subsets/{dataset}.csv')
                df = prepare_datatypes(feature_df, self.area)
                df = drop_excess_labels(df)

                if dataset in PER_CAPITA_FEATS: # adjust per capita
                    df = adjust_per_capita(df, pop)

                self.trips_df = self.trips_df.join(df, how="outer")
        self.trips_df = drop_excess_labels(self.trips_df).dropna(axis=0)    
        return self.trips_df
    

    def get_features(self):
        return self.trips_distance
    
    
