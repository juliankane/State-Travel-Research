
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Travel.TravelDistance import TravelDistance
from LinearRegression import LR_Model


def exclude_feature_comparisons(data, mask = [], feats = []):
    exclude = []

    for fee in feats:
        for tee in feats:
            index1 = data.columns.get_loc(fee)
            index2 = data.columns.get_loc(tee)
            mask[index1,index2] = True
            mask[index1, index2] = True
    return mask




td = TravelDistance(area="Region")
travel = td.load_feature_data(exclude=["poverty","airports", "gdp", "airports", "Diesel", "Other"], include_age = True)

# load cor_eff
cor_eff = travel.corr(numeric_only=True)

# create subplot
_, ax = plt.subplots(figsize=(10,10))

# get mask - bottom half
mask = np.triu(np.ones_like(cor_eff, dtype=bool))
#mask = exclude_feature_comparisons(cor_eff, mask = mask, feats=td.get_features())

# heatmap
sns.heatmap(cor_eff,linecolor='white',linewidths=1,mask=mask, ax=ax, annot=True,cmap="rocket_r")
plt.show()

g = sns.pairplot(travel, vars=['T. personal expenditures', 'Diesel', 'Electric (EV)', 'Gasoline'])
#plt.show()


'''
Train model to game more insights into the data

Linear-Regression - 

'''
lr = LR_Model(travel)

feat = td.get_features()
for f in feat:
    lr.do_regression('Diesel',predict_idx=f)
















