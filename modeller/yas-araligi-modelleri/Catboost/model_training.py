import xgboost as xgb
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import optuna
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report 
file_path = '/content/Final.xlsx'
data = pd.read_excel(file_path)

X = data.drop(columns=['Dosya Adı', 'Önerilen Yaş Aralığı'])
y = data['Önerilen Yaş Aralığı']

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
import optuna
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2)


params = {'iterations': 178,
          'depth': 4,
          'learning_rate': 0.0316023136178663,
          'l2_leaf_reg': 0.016961644557040984}
model = CatBoostClassifier(**params, verbose=0)
model.fit(X_train, y_train)
preds = model.predict(X_test)
accuracy = accuracy_score(y_test, preds)
print(f"Test Accuracy: {accuracy}")