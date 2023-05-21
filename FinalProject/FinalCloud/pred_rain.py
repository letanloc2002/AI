import numpy as np 
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
data_train = pd.read_csv(".\data\weather-main.csv")
data_train = np.array(data_train)
print(data_train.shape)
X = data_train[:, :5]
Y_tomorrow = data_train[:, 5]
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, Y_tomorrow)
def get_result(temp, wind, cloud, hud, pressure):
    return (neigh.predict([[temp, wind, cloud, hud, pressure]])[0]) == 1

"""
used: 
import pred_rain as model
result = model.get_result(temp, wind, cloud, hud, pressure)
if(result):
    print("rain")
else:
    print("sunny")
"""