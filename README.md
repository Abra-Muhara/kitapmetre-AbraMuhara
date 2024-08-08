

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
  4. Uygulama aracılığıyla kullanıcıya kitap hakkında elde edilen verilerin bildirilmesi.
 ## Projedeki modellerin açıklaması
 1. Cümlelerin Uygunsuzluklarını ölçmek:
	 1. **ANN**:



	![ANN Mimarisi](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/ofansif_model.h5.png)

  
## Veri Seti ve Araçlar
Kitap Veri Seti Oluşturma Aracı Web Sitesi Linki:
https://kitapmetre-veri-seti-araci.glitch.me

Yaş Aralığı Sınıflandırma: https://huggingface.co/AbraMuhara/RandomForestAgeClassificationTDDI2024

Uygunsuz Cümle Sınıflandırma: https://huggingface.co/AbraMuhara/Fine-TunedBERTURKOfansifTespit


Kaynakçalar:
ATEŞMAN, Ender. (1997). Türkçe’de okunabilirliğin Ölçülmesi. A.Ü. 		 					Tömer Dil Dergisi, sayı:58,s.171-174.

Cetinkaya, B. (2008). Türkçe Metinlerde Okunabilirlik Analizi.

Flesch, R. (1948). A New Readability Yardstick. Journal of Applied Psychology, 32(3), 221-233. https://doi.org/10.1037/h0057532
