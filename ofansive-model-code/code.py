import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import *

data = pd.read_csv("/kaggle/input/turkish-offensive-language-detection/train.csv")
test_data = pd.read_csv("/kaggle/input/turkish-offensive-language-detection/test.csv")

#data['label'] = data['label'].map({'0': 0, '1': 1})
#test_data['label'] = test_data['label'].map({'0': 0, '1': 1})

texts = data['text']
labels = data['label']

test_texts = test_data['text']
test_labels = test_data['label']

label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(labels)
test_labels = label_encoder.transform(test_labels)

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(texts)
X_test = vectorizer.transform(test_texts)

model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.001), metrics=['accuracy'])

early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

history = model.fit(X_train, labels, epochs=10, batch_size=32, validation_split=0.1, callbacks=[early_stopping])

loss, accuracy = model.evaluate(X_test, test_labels)
print(f'Test seti doğruluğu: {accuracy}')

model.save("ofansif_model.h5")

with open("vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)
