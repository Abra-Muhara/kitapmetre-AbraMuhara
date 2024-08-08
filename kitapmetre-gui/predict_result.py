import re
import customtkinter
from customtkinter import *
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import emoji
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
from zemberek import (
    TurkishSpellChecker,
    TurkishSentenceNormalizer,
    TurkishSentenceExtractor,
    TurkishMorphology,
    TurkishTokenizer
)
import pdfplumber

tokenizer = AutoTokenizer.from_pretrained("modeller/uygunsuzluk-modelleri/BERTURK-FineTuned/tokenizer")
model = AutoModelForSequenceClassification.from_pretrained("modeller/uygunsuzluk-modelleri/BERTURK-FineTuned/model")

morph = TurkishMorphology.create_with_defaults()
dosya = open("uygunsuz-kelime-listesi/ofansif.txt", "r", encoding='utf-8')
yasaKelimeler = dosya.read().split('\n')
dosya.close()
rf = joblib.load("modeller/yas-araligi-modelleri/Random Forest (Kullanılan)/random_forest_model.pkl")
label_encoder = joblib.load("modeller/yas-araligi-modelleri/Random Forest (Kullanılan)/random_forest_label_encoder.pkl")


def clean_text(text):
    text = text.lower()
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = emoji.replace_emoji(text, replace='')
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def kelime_analizi(word):
    results = morph.analyze(word)
    ans = ""
    for result in results:
        ans = str(result)
    try:
        return (ans[1:ans.index(':')])
    except:
        return " "


def count_syllables(word):
    vowels = "aeıioöuü"
    syllables = 0
    word = word.lower()
    for char in word:
        if char in vowels:
            syllables += 1
    return max(syllables, 1)


def analyze_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    text = clean_text(text)
    sentences = re.split(r'[.!?]+', text)
    sentences = [sentence.strip() for sentence in sentences if sentence]

    words = re.findall(r'\b\w+\b', text)
    syllable_count = sum(count_syllables(word) for word in words)
    offensiveWordCount = 0
    for word in words:
        root = kelime_analizi(word.lower())
        root = root.lower()
        if root in yasaKelimeler:
            offensiveWordCount += 1

    sentence_count = len(sentences)
    word_count = len(words)

    avg_words_per_sentence = word_count / sentence_count if sentence_count > 0 else 0
    avg_syllables_per_word = syllable_count / word_count if word_count > 0 else 0
    avg_syllables_per_sentence = syllable_count / sentence_count if sentence_count > 0 else 0
    avg_offensive_per_word = offensiveWordCount / word_count if word_count > 0 else 0
    odds = offensiveWordCount / (word_count - offensiveWordCount) if (word_count - offensiveWordCount) > 0 else 0
    atesman_score = 198.825 - 40.175 * avg_syllables_per_word - 2.610 * avg_words_per_sentence
    FRES = 206.835 - (avg_words_per_sentence * 1.015) + (avg_syllables_per_word * 8.46)
    cetinkaya_uzun = 118.823 - (25.987 * avg_syllables_per_word) - (0.971 * avg_words_per_sentence)

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
        'FRES': FRES,
        'CetinKayaOP': cetinkaya_uzun
    }


# Cümleyi sınıflandırma fonksiyonu
def classify_sentence(sentence, state):
    inputs = tokenizer(sentence, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    logits = outputs.logits
    probabilities = torch.softmax(logits, dim=-1)
    if state == 1:
        class_index = probabilities[0][1].item()
        return class_index
    return torch.argmax(probabilities, dim=-1).item()


def predict_ans(file_path):
    wait_page = CTk()
    wait_page.geometry("400x300")
    wait_page.title("Lütfen Bekleyin")
    label = CTkLabel(master=wait_page, text="Lütfen bekleyin...")
    label.configure(font=CTkFont(family="Arial", size=30))
    label.place(relx=0.5, rely=0.5, anchor="center")

    def update_wait_page():
        if label.cget("text") == "Lütfen bekleyin...":
            label.configure(text="Lütfen bekleyin.")
        elif label.cget("text") == "Lütfen bekleyin.":
            label.configure(text="Lütfen bekleyin..")
        else:
            label.configure(text="Lütfen bekleyin...")
        wait_page.after(500, update_wait_page)

    wait_page.after(500, update_wait_page)
    wait_page.update()

    result = analyze_text_from_pdf(file_path)
    temp = 0
    offensive_count = 0
    for sentence in result['sentences']:
        temp += classify_sentence(sentence, 1)
        offensive_count += classify_sentence(sentence, 0)
    offensive_general = temp / result['sentence_count']
    offensive_ratio = offensive_count / result['sentence_count'] if result['sentence_count'] > 0 else 0
    offensive_by_non_offensive = offensive_count / (result['sentence_count'] - offensive_count)

    df = pd.DataFrame([{
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
        'Ortalama Cümle Ofansifliği': offensive_general
    }])

    df_for_prediction = df.drop(["Dosya Adı"], axis=1)

    predictions = rf.predict(df_for_prediction)

    predicted_labels = label_encoder.inverse_transform(predictions)

    predicted_age_range = predicted_labels[0]

    print(predicted_age_range)

    wait_page.destroy()

    result_page = CTk()
    result_page.title("Kitap İncelemesi")
    result_page.geometry("800x600")
    result_page.minsize(650, 600)

    frame = CTkScrollableFrame(result_page, border_color = "#1fb87d", border_width = 2, width=600, 
                     height=450, scrollbar_button_color="#15bf70", scrollbar_button_hover_color="#0ceb95")
    frame.place(relx = 0.5, rely = 0.5, anchor = "center")
    for i in range(len(file_path)):
        if file_path[i] == '/':
            indx = i
    name = file_path[indx+1:file_path.index(".pdf")]

    main_font = CTkFont(family="Arial", size=25)
    txt_font = CTkFont(family="Arial", size=20)

    name_label = CTkLabel(result_page, text = name,  font=main_font)
    name_label.place(relx = 0.5, rely = 0.05, anchor = "center")

    age_label = CTkLabel(frame, text = f"Kitabın yaş aralığı: {predicted_age_range}", 
                         font = txt_font)
    age_label.pack(pady = 10, padx = 15)

    w_label = CTkLabel(frame, text = f"Toplam Kelime Sayısı: {result['word_count']}", 
                         font = txt_font)
    w_label.pack(pady = 10, padx = 15)

    s_label = CTkLabel(frame, text = f"Toplam Cümle Sayısı: {result['sentence_count']}", 
                         font = txt_font)
    s_label.pack(pady = 10, padx = 15)

    o_w_label = CTkLabel(frame, text = f"Uygunsuz Kelime Sayısı: {result['offensive_word_count']}", 
                         font = txt_font)
    o_w_label.pack(pady = 10, padx = 15)

    o_s_label = CTkLabel(frame, text = f"Uygunsuz Cümle Sayısı: {offensive_count}", 
                         font = txt_font)
    o_s_label.pack(pady = 10, padx = 15)

    offensive_ratio = CTkLabel(frame, text = f"Kitabın Uygunsuzluk Oranı: {round(offensive_general, 5)}", 
                         font = txt_font)
    offensive_ratio.pack(pady = 10, padx = 15)

    syllable_count = CTkLabel(frame, text = f"Toplam Hece Sayısı: {result['syllable_count']}", 
                         font = txt_font)
    syllable_count.pack(pady = 10, padx = 15)

    veri  = CTkLabel(frame, text = f"Cümle Başına Ortalama Kelime Sayısı: {round(result['avg_words_per_sentence'],4)}", 
                         font = txt_font)
    veri.pack(pady = 10, padx = 15)

    veri1  = CTkLabel(frame, text = f"Cümle Başına Ortalama Hece Sayısı: {round(result['avg_syllables_per_sentence'],4)}", 
                         font = txt_font)
    veri1.pack(pady = 10, padx = 15)

    veri2  = CTkLabel(frame, text = f"Ateşman Okunabilirlik Puanı: {round(result['atesman_score'],4)}", 
                         font = txt_font)
    veri2.pack(pady = 10, padx = 15)

    veri3 = CTkLabel(frame, text = f"Ofansif Cümle Yüzdesi: {round(offensive_by_non_offensive,6)}", 
                         font = txt_font)
    veri3.pack(pady = 10, padx = 15)

    veri4 = CTkLabel(frame, text = f"Ofansif Kelime Oranı: {round(result['avg_offensive_per_word'],6)}", 
                         font = txt_font)
    veri4.pack(pady = 10, padx = 15)

    veri5 = CTkLabel(frame, text = f"Ofansif Kelimelerin Olmayanlara Oranı: {round(result['odds_offensive'],6)}", 
                         font = txt_font)
    veri5.pack(pady = 10, padx = 15)

    veri6 = CTkLabel(frame, text = f"FRES Okunulabilirlik Puanı: {round(result['FRES'],4)}", 
                         font = txt_font)
    veri6.pack(pady = 10, padx = 15)

    veri7 = CTkLabel(frame, text = f"Çetinkaya Uzun Okunulabilirlik Puanı: {round(result['CetinKayaOP'],4)}", 
                         font = txt_font)
    veri7.pack(pady = 10, padx = 15)

    info = CTkLabel(result_page, text = "0.00 : %0, 1.00 : %100", font = CTkFont(family="Arial", size=15))
    info.place(relx = 0.9, rely = 0.95, anchor = "se")

    result_page.mainloop()
