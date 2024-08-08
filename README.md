
# kitapmetre-2024AcikHackTDDI

## Bu proje Teknofest Doğal Dil İşleme Yarışması için yapılmıştır.
(https://www.teknofest.org/tr/yarismalar/turkce-dogal-dil-isleme-yarismasi/)

## Takım Bilgileri:
  Takım Adı: Abra Muhara
  Takım ID: #561838
  Başvuru ID: #2290264
  Hugging Face: https://huggingface.co/AbraMuhara
  Github: https://github.com/Abra-Muhara
## Takım üyeleri:
  Fatih Kürşat Cansu(Danışman)
  Şuayp Talha Kocabay(Kaptan): https://github.com/suayptalha
  Mehmet Kağan ALBAYRAK(Üye): https://github.com/TFLkedimestan
## Problem:
  Ele  alınan problem, özellikle  çocuk ve genç okurlar için  uygun  kitapların  seçilmesi  sürecindeki eğitimcilerin ve yetişkinlerin yaşadıkları belirsizliktir.

Kitapların  içerdiği  dil, temalar  ve  uygunsuz  öğeler, yaş  gruplarına  göre  farklı  etkiler  yaratmaktadır.

Bu bağlamda, öğretmenler, kütüphaneciler, ebeveynler  ve okurlar için  kitapların  içeriklerinin  değerlendirilmesi  ve  uygunluk  derecelerinin  belirlenmesi  oldukça  önem  arz etmektedir
## Projemizin Aşamaları:
  Projemizin hedefi, sisteme atılan kitabın yaş aralığını **0-8, 8-12, 12-15, 15-18 ve 18+** olarak sınıflandırması
Projemizin Aşamaları:
  1. İnce ayar yapılmış **BERTURK** ile cümleleri uygunsuzluklarına göre sınıflandırması
  2. **Kendi yazdığımız kelime listesi** ile kelimeleri uygunsuzluklarına göre sınıflandırması
  3. İlk 2 aşamada elde ettiğimiz verilerin yanı sıra Cümle Sayısı, Hece Sayısı, Cümle Başına Ortalama Kelime Sayısı, Cümle Başına Ortalama Hece Sayısı, Ateşman OP(Okunabilirlik Puanı), Uygunsuz Cümle Sayısı, Uygunsuz Cümle Sayısının Toplam Cümle Sayısına Oranı, Uygunsuz Cümle Yüzdesi, Uygunsuz Kelime Sayısı, Uygunsuz Kelime Sayısının Toplam Kelime Sayısına Oranı, Uygunsuz Kelime Sayısının Uygunsuz Olmayan Kelime Sayısına oranı, FRES Puanı, Çetinkaya Uzun OP ve Ortalama Cümle Uygunsuzluk Değeri ile yaş konusunda sınıflandırma yapmaktır.
 ## Projedeki modellerin açıklaması
 1. Cümlelerin Uygunsuzluklarını ölçmek:
	 a. **ANN**
		 Modelimizin mimarisi:
			  Dense(64)
			  Dropout(0.5)
			  Dense(32)
			  Dropout(0.5)
			  Dense(1, activation="sigmoid")
## Veri Seti ve Araçlar
Kitap Veri Seti Oluşturma Aracı Web Sitesi Linki:
https://kitapmetre-veri-seti-araci.glitch.me

Yaş Aralığı Sınıflandırma: https://huggingface.co/AbraMuhara/RandomForestAgeClassificationTDDI2024

Uygunsuz Cümle Sınıflandırma: https://huggingface.co/AbraMuhara/Fine-TunedBERTURKOfansifTespit


Kaynakçalar:
ATEŞMAN, Ender. (1997). Türkçe’de okunabilirliğin Ölçülmesi. A.Ü. Tömer Dil Dergisi, sayı:58,s.171-174.


