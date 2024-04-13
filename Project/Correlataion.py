from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from Project.Travel import TravelDistance


trips_labels = ['Number of Trips >=500', 'Number of Trips 250-500', 'Number of Trips 100-250']


def exclude_feature_comparisons(data, mask = [], feats = []):
    exclude = []

    for fee in feats:
        for tee in feats:
            index1 = data.columns.get_loc(fee)
            index2 = data.columns.get_loc(tee)

            mask[index1,index2] = True
            mask[index1, index2] = True
    return mask

TravelDistance = TravelDistance.load_state_data(type="noagesex")

# load cor_eff
cor_eff = TravelDistance.corr(numeric_only=True)

# create subplot
_, ax = plt.subplots(figsize=(10,10), constrained_layout=True)

# get mask - bottom half
mask = np.triu(np.ones_like(cor_eff, dtype=bool))
mask = exclude_feature_comparisons(cor_eff, mask = mask, feats=trips_labels)

# heatmap
sns.heatmap(cor_eff,linecolor='white',linewidths=1,mask=mask, ax=ax, annot=True,cmap="rocket_r")
plt.show()

g = sns.pairplot(TravelDistance)
plt.show()




'''

Train model to game more insights into the data

Linear-Regression - 

'''

















