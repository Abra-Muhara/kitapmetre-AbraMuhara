import pandas as pd
import sklearn
import tensorflow
import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import BaggingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, f1_score
from sklearn.ensemble import AdaBoostClassifier
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib
from sklearn.metrics import accuracy_score, f1_score
from sklearn.experimental import enable_hist_gradient_boosting  # Histogram tabanlı GB'yi etkinleştirin
from sklearn.ensemble import HistGradientBoostingClassifier
rawData = pd.read_excel("kitap-veri-seti/Final.xlsx")
rawY=rawData["Önerilen Yaş Aralığı"]
rawX=(rawData.drop("Dosya Adı",axis=1)).drop("Önerilen Yaş Aralığı",axis=1)
label_encoder = LabelEncoder()
Y=label_encoder.fit_transform(rawY)
X_train, X_test, y_train, y_test = train_test_split(rawX, Y, test_size=0.2, random_state=42)
model = HistGradientBoostingClassifier(
    max_iter=500,
    learning_rate=0.2,
    max_depth=500,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')

print(f'Histogram Tabanlı Gradient Boosting - Doğruluk: {accuracy}')
print(f'Histogram Tabanlı Gradient Boosting - F1 Skoru: {f1}')

joblib.dump(model,"hist.pkl")
