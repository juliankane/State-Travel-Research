from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from Travel.TravelDistance import TravelDistance


def exclude_feature_comparisons(data, mask = [], feats = []):
    exclude = []

    for fee in feats:
        for tee in feats:
            index1 = data.columns.get_loc(fee)
            index2 = data.columns.get_loc(tee)
            mask[index1,index2] = True
            mask[index1, index2] = True
    return mask


td = TravelDistance()
travel = td.load_feature_data()

# load cor_eff
cor_eff = travel.corr(numeric_only=True)

# create subplot
_, ax = plt.subplots(figsize=(10,10), constrained_layout=True)

# get mask - bottom half
mask = np.triu(np.ones_like(cor_eff, dtype=bool))
mask = exclude_feature_comparisons(cor_eff, mask = mask, feats=td.get_features())

# heatmap
sns.heatmap(cor_eff,linecolor='white',linewidths=1,mask=mask, ax=ax, annot=True,cmap="rocket_r")
plt.show()

g = sns.pairplot(travel)
plt.show()




'''

Train model to game more insights into the data

Linear-Regression - 

'''

















