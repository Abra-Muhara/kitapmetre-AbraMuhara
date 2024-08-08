


# kitapmetre-2024AcikHackTDDI

## Bu proje Teknofest Doğal Dil İşleme Yarışması için yapılmıştır.
(https://www.teknofest.org/tr/yarismalar/turkce-dogal-dil-isleme-yarismasi/)

## Takım Bilgileri:
![Takım logosu](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/ABRA%20MUHARA.png)

  Takım Adı: Abra Muhara
  
  Takım ID: #561838
  
  Başvuru ID: #2290264
  
  Hugging Face: https://huggingface.co/AbraMuhara
  
  Github: https://github.com/Abra-Muhara
## Takım üyeleri:
  Fatih Kürşat Cansu(Danışman)
  
  Şuayp Talha Kocabay(Kaptan): https://github.com/suayptalha
  
  Mehmet Kağan Albayrak(Üye): https://github.com/TFLkedimestan
## Problem:
  Ele  alınan problem, özellikle  çocuk ve genç okurlar için  uygun  kitapların  seçilmesi  sürecindeki eğitimcilerin ve yetişkinlerin yaşadıkları belirsizliktir.

Kitapların  içerdiği  dil, temalar  ve  uygunsuz  öğeler, yaş  gruplarına  göre  farklı  etkiler  yaratmaktadır.

Bu bağlamda, öğretmenler, kütüphaneciler, ebeveynler  ve okurlar için  kitapların  içeriklerinin  değerlendirilmesi  ve  uygunluk  derecelerinin  belirlenmesi  oldukça  önem  arz etmektedir
## Projenin Tanımı:
Bu proje, kullanıcıların sisteme yükledikleri Türkçe kitapların PDF dosyalarını analiz ederek kitapların uygun yaş aralıklarını, içerilerinde kaç uygunsuz cümle ve kelime geçtiği vb. bilgileri belirlemeyi ve bunları kullanıcıya bildirmeyi amaçlayan bir uygulamadır.

Bu projenin ana teması, kitapların içerdiği dil ve temaların uygunluğunu değerlendirerek okurların ve eğitimcilerin doğru seçimler yapmasını sağlamaktır. Elde edilen bulgular doğrultusunda proje bu amaca yüksek bir doğrulukla ulaşmaktadır.
## Projenin Sağladığı Çözüm ve Hedef Kitlesi
Bu proje kitapların içeriğini analiz ederek kitaplar hakkında çeşitli bilgiler ve sonuçlar çıkartıp bunları kullanıcıya vermektedir. Bu sayede kullanıcı okuyacağı veya önereceği kitap hakkında derinlemesine bilgi sahibi olmaktadır. Uygulamanın verdiği yaş aralığı sayesinde uygun kitapları önerebilecek veya okuyabilecektir.

Proje, kitap bulma ve önerme bakımında zorluk yaşayan kişilere yöneliktir.

Bu projenin hedef kitlesi şunlardır:

•Kültür ve Turizm Bakanlığına bağlı halk kütüphanelerinde çalışan kütüphaneciler,

•Milli Eğitim Bakanlığına bağlı öğretmenler,

•Eğitimciler,

•Çocuklarına kitap önerecek olan ebeveynler,

•Okurlar.
## Proje İş Akışı
![Projenin başarıyla tamamlanması için gereken görevlerin ve süreçler](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/workflow.png)

## Projemizin Aşamaları:
  Projemizin hedefi:
  Sisteme atılan kitabın yaş aralığını **0-8, 8-12, 12-15, 15-18 ve 18+** olarak sınıflandırması ve kullanıcıya kitap hakkında birçok veriyi bildirmesi.
Projemizin Aşamaları:	
  1. Uygulama aracılığıyla kullanıcıdan kitap PDF'inin alınması ve bu PDF'in metine çevrilmesi.
  2. İnce ayar yapılmış **BERTURK** ile cümleleri uygunsuzluklarına göre sınıflandırması.
  3. **Kendi yazdığımız kelime listesi** ile kelimeleri uygunsuzluklarına göre sınıflandırması.
  4. İlk 2 aşamada elde ettiğimiz verilerin yanı sıra kitapların cümle sayısı, hece sayısı, cümle başına ortalama kelime sayısı, cümle başına ortalama hece sayısı, Ateşman OP(Okunabilirlik Puanı), uygunsuz cümle sayısı, uygunsuz cümle sayısının toplam cümle sayısına oranı, uygunsuz cümle yüzdesi, uygunsuz kelime sayısı, uygunsuz kelime sayısının toplam kelime sayısına oranı, uygunsuz kelime sayısının uygunsuz olmayan kelime sayısına oranı, FRES puanı, Çetinkaya Uzun okunulabilirlik puanı ve ortalama cümle uygunsuzluk değeri ile yaş aralığı sınıflandırması yapılması.
  5. Uygulama aracılığıyla kullanıcıya kitap hakkında elde edilen verilerin bildirilmesi.
  
## Veri Seti ve Araçlar
Kitap Veri Seti Oluşturma Aracı Web Sitesi Linki:
https://kitapmetre-veri-seti-araci.glitch.me

Yaş Aralığı Sınıflandırma: https://huggingface.co/AbraMuhara/RandomForestAgeClassificationTDDI2024

Uygunsuz Cümle Sınıflandırma: https://huggingface.co/AbraMuhara/Fine-TunedBERTURKOfansifTespit

## Modellerin Oluşturulması
Metinlerin uygunsuzluğunu ölçen model için çeşitli mimariler kullanılmıştır.
Bunlar:

•ANN:
Bahsi geçen modellerden ilki olan ve metinlerin uygunsuzluk düzeylerini ölçen model için farklı mimariler kullanan 4 model oluşturulmuştur. Bunlar BERT, BERT-Turkish, RNN ve kendimizin oluşturduğu bir ANN modelidir.

İlk olarak deneme amaçlı bir ANN oluşturup eğiterek %89,42 doğrulukla ve 0.3972 loss ile çalıştığına ulaşıldı. Fakat büyük veya karmaşık bağlamlı metinlerde sorun çıkarttığı için bu model kullanılmamıştır.

![Modelin Hiperparametreleri](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/ann.png)

•RNN:

Ardından 4 GRU (Geçitli Tekrarlayan Birim) katmanlı bir RNN (Yinelemeli Sinir Ağı) oluşturulmuştur. Optimizasyon algoritması olarak aşırı öğrenmeyi azaltıp daha hızlı ve kararlı öğrenme sağlayan AdamW kullanılmıştır. İlk olarak 4 epoch’a kadar eğitilmiştir. Ardından Early Stopping kullanılmış ve 6. epoch’ta  loss arttığı için eğitim durdurulmuştur. Model %89,83 doğrulukla çalışmaktadır. Ancak BERT ile yapılan model daha yüksek doğrulukla çalıştığı için bu modeli kullanılmamıştır.

![Modelin Hiperparametreleri](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/rnn.png)

![Çeşitli Epoch Değerlerinde RNN Modelinin Doğruluk Değerleri](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/accuracy.png)

![Çeşitli Epoch Değerlerinde RNN Modelininin Kayıp Değerleri](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/loss.png)

•BERT:

•BERT-Turkish:


Bu 

Kaynakçalar:
ATEŞMAN, Ender. (1997). Türkçe’de okunabilirliğin Ölçülmesi. A.Ü. 		 					Tömer Dil Dergisi, sayı:58,s.171-174.

Cetinkaya, B. (2008). Türkçe Metinlerde Okunabilirlik Analizi.

Flesch, R. (1948). A New Readability Yardstick. Journal of Applied Psychology, 32(3), 221-233. https://doi.org/10.1037/h0057532
