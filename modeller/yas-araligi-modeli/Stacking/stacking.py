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
from sklearn.ensemble import VotingClassifier, RandomForestClassifier, BaggingClassifier, AdaBoostClassifier
from xgboost import XGBClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
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
rawData = pd.read_excel("Final.xlsx")
rawY=rawData["Önerilen Yaş Aralığı"]
rawX=(rawData.drop("Dosya Adı",axis=1)).drop("Önerilen Yaş Aralığı",axis=1)
label_encoder = LabelEncoder()
Y=label_encoder.fit_transform(rawY)
X_train, X_test, y_train, y_test = train_test_split(rawX, Y, test_size=0.2, random_state=42)

from sklearn.ensemble import StackingClassifier
print("Stacking Classify with same as up")
xgb_model = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss', random_state=42)
rf_model = RandomForestClassifier(n_estimators=50, random_state=42)
adaboost_model = AdaBoostClassifier(base_estimator=rf_model, n_estimators=50, random_state=42)
bagging_model = BaggingClassifier(base_estimator=rf_model, n_estimators=50, random_state=42)

# Meta (Stacking) modeli oluştur
stacking_clf = StackingClassifier(
    estimators=[
        ('xgb', xgb_model),
        ('rf', rf_model),
        ('adaboost', adaboost_model),
        ('bagging', bagging_model)
    ],
    final_estimator=LogisticRegression(),
    cv=5,  # Cross-validation katman sayısı
    stack_method='auto',  # 'predict_proba' veya 'predict' ile tahminler
    passthrough=True,  # Baz modellerin tahminlerini doğrudan meta modeline geçirme
    n_jobs=-1  # Çoklu işlem
)

# Modeli eğit
stacking_clf.fit(X_train, y_train)

# Tahmin yap
y_pred = stacking_clf.predict(X_test)

# Performansı değerlendir
accuracy = accuracy_score(y_test, y_pred)
print(f"Doğruluk: {accuracy:.2f}")
joblib.dump(stacking_clf,"STACKING.pkl")




