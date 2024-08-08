import re
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import zemberek
import emoji
from zemberek import (
    TurkishSpellChecker,
    TurkishSentenceNormalizer,
    TurkishSentenceExtractor,
    TurkishMorphology,
    TurkishTokenizer
)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'@[\w_]+', '', text)
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = emoji.replace_emoji(text, replace='')
    text = re.sub(r'\s+', ' ', text).strip()
    return text
morph = TurkishMorphology.create_with_defaults()
def kelime_analizi(word):
    results = morph.analyze(word)
    ans = ""
    for result in results:
      ans = str(result)
    try:
      return (ans[1:ans.index(':')])
    except:
      return " "


# Heceleri sayma fonksiyonu
def count_syllables(word):
    vowels = "aeıioöuü"
    syllables = 0
    word = word.lower()
    for char in word:
        if char in vowels:
            syllables += 1
    return max(syllables, 1)
dosya=open("uygunsuz-kelime-listesi/ofansif.txt","r",encoding='utf-8')
yasaKelimeler=dosya.read().split('\n')
# Metni analiz etme fonksiyonu
def analyze_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().replace('\n',' ')
    text=clean_text(text)
    sentences = re.split(r'[.!?]+', text)
    sentences = [sentence.strip() for sentence in sentences if sentence]

    words = re.findall(r'\b\w+\b', text)

    syllable_count = sum(count_syllables(word) for word in words)
    offensiveWordCount=0
    for word in words:
        root=kelime_analizi(word.lower())
        root=root.lower()
        if root in yasaKelimeler:
            offensiveWordCount+=1
    sentence_count = len(sentences)
    word_count = len(words)

    avg_words_per_sentence = word_count / sentence_count if sentence_count > 0 else 0
    avg_syllables_per_word = syllable_count / word_count if word_count > 0 else 0
    avg_syllables_per_sentence = syllable_count / sentence_count if sentence_count > 0 else 0
    avg_offensive_per_word = offensiveWordCount/word_count if word_count > 0 else 0
    odds=offensiveWordCount/(word_count-offensiveWordCount) if (word_count-offensiveWordCount)>0 else 0
    atesman_score = 198.825 - 40.175 * avg_syllables_per_word - 2.610 * avg_words_per_sentence
    FRES= 206.835-(avg_words_per_sentence*1.015)+(avg_syllables_per_word*8.46)
    cetinkaya_uzun = 118.823 - (25.987*avg_syllables_per_word)-(0.971*avg_words_per_sentence)
    return {
        'sentences': sentences,
        'sentence_count': sentence_count,
        'word_count': word_count,
        'syllable_count': syllable_count,
        'avg_words_per_sentence': avg_words_per_sentence,
        'avg_syllables_per_sentence': avg_syllables_per_sentence,
        'atesman_score': atesman_score,
        'offensive_word_count': offensiveWordCount,
        'avg_offensive_per_word': avg_offensive_per_word,
        'odds_offensive': odds,
        'FRES':FRES,
        'CetinKayaOP':cetinkaya_uzun
    }

tokenizer = AutoTokenizer.from_pretrained("C:/Users/PC/Downloads/analiz1/wetransfer_data_2024-08-01_1437/tokenizer")
model = AutoModelForSequenceClassification.from_pretrained("modeller/uygunsuzluk-modelleri/BERTURK-FineTuned/model")

# Cümleyi sınıflandırma fonksiyonu
def classify_sentence(sentence,state):
    inputs = tokenizer(sentence, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    logits = outputs.logits
    probabilities = torch.softmax(logits, dim=-1)
    if(state==1):
        class_index = probabilities[0][1].item()
        return class_index
    return torch.argmax(probabilities, dim=-1).item()

df = pd.DataFrame(columns=[
    'Dosya Adı', 'Cümle Sayısı', 'Hece Sayısı', 'Cümle Başına Ortalama Kelime Sayısı',
    'Cümle Başına Ortalama Hece Sayısı', 'Ateşman Okunabilirlik Puanı', 'Ofansif Cümle Sayısı',
    'Ofansif Cümle Oranı', 'Ofansif Cümle Yüzdesi','Ofansif Kelime Sayısı','Ofansif Kelime Oranı','Kelime Sayısı',
    'Ofansif Kelime Sayısının Ofansif Olmayan Kelime Sayısına oranı','FRES','CetinKayaUzun','Offensive General'
])
import os

folder_path = 'C:/Users/PC/Downloads/analiz1/wetransfer_data_2024-08-01_1437/BookData/Yas15-18'
file_paths = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
print(file_paths)
for file_path in file_paths:
    print(file_path)
    result = analyze_text(file_path)
    temp=0
    offensive_count=0
    for sentence in result['sentences']:
        temp+=classify_sentence(sentence,1)
        offensive_count+=classify_sentence(sentence,0)
    offensive_general= temp/result['sentence_count']
    offensive_ratio = offensive_count / result['sentence_count'] if result['sentence_count'] > 0 else 0
    offensive_by_non_offensive = offensive_count/(result['sentence_count']-offensive_count)

    df = df.append({
        'Dosya Adı': file_path,
        'Cümle Sayısı': result['sentence_count'],
        'Hece Sayısı': result['syllable_count'],
        'Cümle Başına Ortalama Kelime Sayısı': result['avg_words_per_sentence'],
        'Cümle Başına Ortalama Hece Sayısı': result['avg_syllables_per_sentence'],
        'Ateşman Okunabilirlik Puanı': result['atesman_score'],
        'Ofansif Cümle Sayısı': offensive_count,
        'Ofansif Cümle Oranı': offensive_ratio,
        'Ofansif Cümle Yüzdesi': offensive_by_non_offensive,
        'Ofansif Kelime Sayısı': result['offensive_word_count'],
        'Ofansif Kelime Oranı': result['avg_offensive_per_word'],
        'Kelime Sayısı': result['word_count'],
        'Ofansif Kelime Sayısının Ofansif Olmayan Kelime Sayısına oranı': result['odds_offensive'],
        'FRES': result['FRES'],
        'CetinKayaUzun': result['CetinKayaOP'],
        'Offensive General': offensive_general

    }, ignore_index=True)

    excel_path = 'results.xlsx'
    df.to_excel(excel_path, index=False)
