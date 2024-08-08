import pandas as pd
import re
import emoji
from sklearn.metrics import classification_report
from transformers import Trainer, TrainingArguments, AutoModel, AutoTokenizer, AutoModelForSequenceClassification
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'@[\w_]+', '', text)
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = emoji.replace_emoji(text, replace='')
    text = re.sub(r'\s+', ' ', text).strip()
    return text

train_data = pd.read_csv('twitter-veri-seti/train.csv')
train_texts = train_data['text'].apply(clean_text)
train_labels = train_data['label']

val_data = pd.read_csv('twitter-veri-seti/valid.csv')
val_texts = val_data['text'].apply(clean_text)
val_labels = val_data['label']

test_data = pd.read_csv('twitter-veri-seti/test.csv')
test_texts = test_data['text'].apply(clean_text)
test_labels = test_data['label']

tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-turkish-128k-uncased")

train_encodings = tokenizer(train_texts.tolist(), truncation=True, padding=True, max_length=512)
val_encodings = tokenizer(val_texts.tolist(), truncation=True, padding=True, max_length=512)
test_encodings = tokenizer(test_texts.tolist(), truncation=True, padding=True, max_length=512)

class OffensiveCommentsDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

train_dataset = OffensiveCommentsDataset(train_encodings, train_labels.tolist())
val_dataset = OffensiveCommentsDataset(val_encodings, val_labels.tolist())
test_dataset = OffensiveCommentsDataset(test_encodings, test_labels.tolist())

model = AutoModelForSequenceClassification.from_pretrained("dbmdz/bert-base-turkish-128k-uncased", num_labels=2)

model.to(device)

training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=64,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=100,
    save_steps=1000,
    save_total_limit=1,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
)

trainer.train()

import shutil
shutil.rmtree('./results', ignore_errors=True)
shutil.rmtree('./logs', ignore_errors=True)
