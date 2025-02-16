import joblib
import pandas as pd
from feature_engineering import DataFrame

data = DataFrame('new_data.csv')
new_data = data.feat_engineer()

y = new_data['quality']
X = new_data.drop(columns=['quality'])

model = joblib.load('Machine_Learning/Supervised_Learning/Classification/Wine_Quality_Classification/model/wine_classification.pkl')
y_pred = model.predict(X)

print(y_pred)