import numpy as np
import pandas as pd
from catboost import CatBoostClassifier, Pool
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
rawData = pd.read_excel("/content/Final.xlsx")
rawY = rawData["Önerilen Yaş Aralığı"]
rawX = rawData.drop(["Dosya Adı", "Önerilen Yaş Aralığı"], axis=1)
X = rawX
Y = rawY
label_encoder = LabelEncoder()
Y = label_encoder.fit_transform(Y)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
train_data = Pool(data=X_train, label=y_train)
test_data = Pool(data=X_test, label=y_test)
model = CatBoostClassifier(
    iterations=1000,
    depth=14,
    learning_rate=0.15,
    loss_function='MultiClass',
    early_stopping_rounds=50,
    verbose=100,
    task_type='GPU'
)
model.fit(
    train_data,
    eval_set=test_data,
    use_best_model=True
)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print("Sınıflandırma Raporu:")
print(report)
