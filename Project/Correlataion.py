from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from Datasets import states


states = states.load_state_data(type="noagesex")


print(states.columns)
print(states.index)
# for col in States.columns:
#     States[col] = pd.to_numeric(States[col], errors="coerce")
    


cor_eff = states.corr(numeric_only=True)

_, ax = plt.subplots(figsize=(6,6))
mask = np.zeros_like(cor_eff)

sns.heatmap(cor_eff,linecolor='white',linewidths=1,mask=mask, ax=ax, annot=True,cmap="rocket_r")
plt.show()

g = sns.pairplot(states, hue='States')
plt.show()







