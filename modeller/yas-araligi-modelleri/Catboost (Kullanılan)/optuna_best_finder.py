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

def objective(trial):
    params = {
        'iterations': trial.suggest_int('iterations', 100, 1000),
        'depth': trial.suggest_int('depth', 3, 10),
        'learning_rate': trial.suggest_loguniform('learning_rate', 1e-3, 1e-1),
        'l2_leaf_reg': trial.suggest_loguniform('l2_leaf_reg', 1e-3, 1e2),
        'loss_function': 'MultiClass'
    }
    
    model = CatBoostClassifier(**params, verbose=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    accuracy = accuracy_score(y_test, preds)
    
    return accuracy

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)

print(f"Best trial: {study.best_trial.params}")
