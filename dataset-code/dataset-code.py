import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import LabelEncoder
import pickle
from keras.models import load_model

import re
import zemberek
from zemberek import (
    TurkishSpellChecker,
    TurkishSentenceNormalizer,
    TurkishSentenceExtractor,
    TurkishMorphology,
    TurkishTokenizer
)

ofansif_kelimeler = []
morph = TurkishMorphology.create_with_defaults()

kelime_path = "/content/ofansif.txt"

with open(kelime_path, "r") as file:
    ofansif_kelimeler = [line.strip() for line in file]

print(ofansif_kelimeler)

with open("/content/ModelData/vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)
model = load_model("/content/ModelData/ofansif_model.h5")


def ofansif_model(metin):
    global model
    global vectorizer
    new_texts = [metin]
    new_X = vectorizer.transform(new_texts)

    predictions = model.predict(new_X.toarray())
    #print(f'Tahmin: {predictions[0][0]:.10f}')
    return predictions[0][0]

def kelime_analizi(word):
    results = morph.analyze(word)
    ans = ""
    for result in results:
      ans = str(result)
    try:
      return (ans[1:ans.index(':')])
    except:
      return " "

def ofansif_mi(cumle):
    kelimeler = re.findall(r'\b\w+\b', cumle.lower())
    return any(kelime_analizi(kelime) in ofansif_kelimeler for kelime in kelimeler)

def metin_analizi(metin):
    cumleler = re.split(r'(?<=[.!?]) +', metin)
    toplam_cumle_sayisi = len(cumleler)

    kelimeler = re.findall(r'\b\w+\b', metin)
    toplam_kelime_sayisi = len(kelimeler)

    toplam_harf_sayisi = sum(len(kelime) for kelime in kelimeler)

    ofansif_cumle_sayisi = 0
    ofansif_kelime_sayisi = 0
    ofansif_kelime_seti = set()

    for cumle in cumleler:
        if ofansif_mi(cumle):
            ofansif_cumle_sayisi += 1
            #print(f"Ofansif Cümle: {cumle}")

            cumledeki_kelimeler = re.findall(r'\b\w+\b', cumle.lower())
            for kelime in cumledeki_kelimeler:
                if kelime in ofansif_kelimeler:
                    #print(f"Ofansif Kelime: {kelime}")
                    ofansif_kelime_seti.add(kelime)
                    ofansif_kelime_sayisi += 1

    iyi_cumle_sayisi = toplam_cumle_sayisi - ofansif_cumle_sayisi
    iyi_kelime_sayisi = toplam_kelime_sayisi - ofansif_kelime_sayisi
    ortalama_kelime_sayisi = toplam_kelime_sayisi / toplam_cumle_sayisi if toplam_cumle_sayisi > 0 else 0
    ortalama_harf_sayisi = toplam_harf_sayisi / toplam_kelime_sayisi if toplam_kelime_sayisi > 0 else 0

    uygunsuzluk_orani = (ofansif_cumle_sayisi / toplam_cumle_sayisi) * 100 if toplam_cumle_sayisi > 0 else 0
    uygunluk_orani = 100 - uygunsuzluk_orani
    okunabilirlik_puani = 198.825 - ((40.175 * ortalama_harf_sayisi) - (2.610*ortalama_kelime_sayisi))
    if okunabilirlik_puani < 0: okunabilirlik_puani = 0

    ofansif_düzey = ofansif_model(metin)

    return {
        "Uygun Cümle Sayısı": iyi_cumle_sayisi,
        "Uygunsuz Cümle Sayısı": ofansif_cumle_sayisi,
        "Toplam Cümle Sayısı": toplam_cumle_sayisi,
        "Uygun Kelime Sayısı": iyi_kelime_sayisi,
        "Uygunsuz Kelime Sayısı": ofansif_kelime_sayisi,
        "Toplam Kelime Sayısı": toplam_kelime_sayisi,
        "Uygun Cümle Sayısının Toplam Cümle Sayısına Oranı": iyi_cumle_sayisi / toplam_cumle_sayisi if toplam_cumle_sayisi > 0 else 0,
        "Uygun Cümle Sayısının Uygunsuz Cümle Sayısına Oranı" : iyi_cumle_sayisi / ofansif_cumle_sayisi if ofansif_cumle_sayisi > 0 else 100,
        #"Toplam Kelime Sayısının Toplam Kelime Sayısına Oranı": toplam_kelime_sayisi / toplam_kelime_sayisi if toplam_kelime_sayisi > 0 else 0,
        "Ortalama Cümledeki Kelime Sayısı": ortalama_kelime_sayisi,
        "Ortalama Kelimedeki Harf Sayısı": ortalama_harf_sayisi,
        "Uygunsuzluk Oranı (Yüzde)": uygunsuzluk_orani,
        "Uygunluk Oranı (Yüzde)": uygunluk_orani,
        "Uygunsuzluk Düzeyi": ofansif_düzey,
        "Okunabilirlik Puanı (OP)" : okunabilirlik_puani
    }

import pdfplumber

def extract_text_from_pdf(pdf_path):
  text = ""

  with pdfplumber.open(pdf_path) as pdf:
    start_page = 3
    end_page = len(pdf.pages) - 1
    for i in range(start_page - 1, end_page):
      page = pdf.pages[i]
      text += page.extract_text()
  return text


import os

excel_path = '/content/Dataset.xlsx'

df = pd.read_excel(excel_path)

kitap_isimleri = df['Kitap Adı'].tolist()

folder_path = '/content/BookData'

dosya_isimleri = os.listdir(folder_path)

print("Başladı")

for kitap_ismi in kitap_isimleri:
    for dosya_ismi in dosya_isimleri:
        if kitap_ismi.lower() in dosya_ismi.lower():
            kitap_path = os.path.join(folder_path, dosya_ismi)
            print(f"Eşleşen Kitap: {kitap_path}")

            book = extract_text_from_pdf(kitap_path)
            sonuc = metin_analizi(book)
            index = df.index[df['Kitap Adı'] == kitap_ismi].tolist()[0]
            for anahtar, deger in sonuc.items():
                df.at[index, anahtar] = deger

            df.to_excel(excel_path, index=False)

            break
