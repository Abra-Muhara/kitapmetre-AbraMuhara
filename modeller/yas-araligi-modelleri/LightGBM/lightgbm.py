import lightgbm as lgb
import pandas as pd
import sklearn
import tensorflow
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
rawData = pd.read_excel("/content/Final.xlsx")
encoder=LabelEncoder()
rawY=rawData["Önerilen Yaş Aralığı"]
Y=encoder.fit_transform(rawY)
rawX=(rawData.drop("Dosya Adı",axis=1)).drop("Önerilen Yaş Aralığı",axis=1)
X_train, X_test, y_train, y_test = train_test_split(rawX, Y, test_size=0.2, random_state=42)
model = lgb.LGBMClassifier(
    boosting_type='gbdt',
    num_leaves=31,
    learning_rate=0.05,
    n_estimators=20
)

# Modeli eğitme
model.fit(X_train, y_train)
report= classification_report(y_test, y_pred, target_names=label_encoder.classes_)
print(report)
model.booster_.save_model('lightgbm_model.txt')