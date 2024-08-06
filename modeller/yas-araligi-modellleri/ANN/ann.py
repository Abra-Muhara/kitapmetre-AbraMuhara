import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import to_categorical

# Veriyi yükle
rawData = pd.read_excel("Final.xlsx")
rawY = rawData["Önerilen Yaş Aralığı"]
rawX = rawData.drop(["Dosya Adı", "Önerilen Yaş Aralığı"], axis=1)

# Özellikler ve etiketler
label_encoder = LabelEncoder()
Y = label_encoder.fit_transform(rawY)
Y = to_categorical(Y)  # One-hot encoding
X = rawX

# Veriyi böl
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Yapay Sinir Ağı modelini tanımla
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    BatchNormalization(),
    Dropout(0.4),  # Dropout oranını düşürdük
    Dense(256, activation='relu'),
    BatchNormalization(),
    Dropout(0.4),
    Dense(512, activation='relu'),
    BatchNormalization(),
    Dropout(0.4),
    Dense(256, activation='relu'),
    BatchNormalization(),
    Dropout(0.4),
    Dense(128, activation='relu'),
    BatchNormalization(),
    Dropout(0.4),
    Dense(Y.shape[1], activation='softmax')  # Çıkış katmanı
])

# Modeli derle
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Erken durdurma (Early stopping)
early_stopping = EarlyStopping(monitor='val_loss', patience=15, restore_best_weights=True)

# Modeli eğit
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, callbacks=[early_stopping], verbose=1)

# Modeli değerlendir
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true = np.argmax(y_test, axis=1)

accuracy = accuracy_score(y_true, y_pred_classes)
f1 = f1_score(y_true, y_pred_classes, average='weighted')
print(f'ANN - Doğruluk: {accuracy:.2f}')
print(f'ANN - F1 Skoru: {f1:.2f}')

# Modeli kaydet
model.save('ann_model.h5')  # Keras modelini h5 formatında kaydet
