import xgboost as xgb
from sklearn.preprocessing import LabelEncoder
import pandas as pd

file_path = '/content/Final.xlsx'
data = pd.read_excel(file_path)

X = data.drop(columns=['Dosya Adı', 'Önerilen Yaş Aralığı'])
y = data['Önerilen Yaş Aralığı']

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

xgb_model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
xgb_model.fit(X_train, y_train)

y_pred = xgb_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=label_encoder.classes_)
