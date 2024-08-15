
# kitapmetre-AbraMuhara

  

## Bu proje TEKNOFEST Doğal Dil İşleme Yarışması için yapılmıştır.

(https://www.teknofest.org/tr/yarismalar/turkce-dogal-dil-isleme-yarismasi/)

  

## Takım Bilgileri:

![Takım logosu](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/ABRA%20MUHARA.png)

  

Takım Adı: Abra Muhara

Takım ID: #561838

Başvuru ID: #2290264

Linkedin: https://www.linkedin.com/company/abra-muhara/

Hugging Face: https://huggingface.co/AbraMuhara

Github: https://github.com/Abra-Muhara

Demo Videonun Linki: https://youtu.be/9p1tD68zZGM?si=8WPXhtJwMStNfqwl

## Takım üyeleri:

Fatih Kürşat Cansu(Danışman)

Şuayp Talha Kocabay(Kaptan): https://github.com/suayptalha

Mehmet Kağan Albayrak(Üye): https://github.com/TFLkedimestan

## Problem:

Ele alınan problem, özellikle çocuk ve genç okurlar için uygun kitapların seçilmesi sürecindeki eğitimcilerin ve yetişkinlerin yaşadıkları belirsizliktir.

  

Kitapların içerdiği dil, temalar ve uygunsuz öğeler, yaş gruplarına göre farklı etkiler yaratmaktadır.

  

Bu bağlamda, öğretmenler, kütüphaneciler, ebeveynler ve okurlar için kitapların içeriklerinin değerlendirilmesi ve uygunluk derecelerinin belirlenmesi oldukça önem arz etmektedir

  

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

### Uygunsuzluk Modeli Veri Seti

**kaggle.com/datasets/toygarr/turkish-offensive-language-detection**

Bu proje için 2 adet veri seti kullanılmıştır. Bunlardan biri Kaggle’dan alınmış olup kullanıcıların Twitter üzerinde paylaştığı ve ‘‘ofansif’’ veya ‘‘ofansif değil’’ olarak sınıflandırılan gönderilerin bulunduğu bir veri setidir. Bu veri setiyle metinlerin ofansif olup olmadığını bulan bir model oluşturulmuştur.

  

İçerisinde;

  

•42.398 adet eğitim verisi,

  

•8.851 adet test verisi,

  

•1.756 adet doğrulama verisi bulunmaktadır.

  

![Veri Seti Veri Dağılımı](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/set-dagilim.png)

  

Veri Seti Veri Dağılımı

  
  

![Eğitim Seti Veri Dağılımı](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/egitim_set.png)

  

Eğitim Seti Veri Dağılımı

  
  

![Test Seti Veri Dağılımı](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/test_set.png)

  

Test Seti Veri Dağılımı

  
  

![Doğrulama Seti Veri Dağılımı](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/valid_set.png)

  

Doğrulama Seti Veri Dağılımı

  

### Yaş Aralığı Modeli Veri Seti

Yaş Aralığı Veri Seti: https://huggingface.co/datasets/AbraMuhara/TurkishBookAgeDataset

Bir diğer veri seti, kelime listesi ve bir önceki veri setiyle oluşturan model ile sıfırdan oluşturulmuştur.

  

İçerisindeki veriler şunlardır:

  

•Cümle, kelime ve hece sayısı;

  

•Cümle başına ortalama kelime ve hece sayısı;

  

•Ofansif cümle sayısı, oranı ve yüzdesi;

  

•Ofansif kelime sayısı ve oranı;

  

•Ofansif kelime sayısının ofansif olmayan kelime sayısına oranı;

  

•Ortalama cümle ofansifliği;

  

•FRES, COE ve Ateşman okunulabilirlik puanları;

  

•Önerilen yaş aralığı.

  

İçerisinde toplam 113 adet kitabın verisi bulunmaktadır.

  

![Veri Seti Yaş Aralığı Dağılımı](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/yas_araligi_dagilim.png)

  

Veri Seti Yaş Aralığı Dağılımı

  
  

![enter image description here](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/yas_veri_ornek.png)

  

Veri Setinden Bir Örnek

  

## Modellerin Oluşturulması

### Modellerin Linkleri

Yaş Aralığı Sınıflandırma: https://huggingface.co/AbraMuhara/AgeClassificationTDDI2024

  

Uygunsuz Cümle Sınıflandırma: https://huggingface.co/AbraMuhara/Fine-TunedBERTURKOfansifTespit

  

### Uygunsuzluk Modelleri

Metinlerin uygunsuzluğunu ölçen model için çeşitli mimariler kullanılmıştır.

Bunlar:

  

•ANN:

Bahsi geçen modellerden ilki olan ve metinlerin uygunsuzluk düzeylerini ölçen model için farklı mimariler kullanan 4 model oluşturulmuştur. Bunlar BERT, BERT-Turkish, RNN ve kendimizin oluşturduğu bir ANN modelidir.

  

İlk olarak deneme amaçlı bir ANN oluşturup eğiterek %89,42 doğrulukla ve 0.3972 loss ile çalıştığına ulaşıldı. Fakat büyük veya karmaşık bağlamlı metinlerde sorun çıkarttığı için bu model kullanılmamıştır.

  

![Modelin Hiperparametreleri](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/ann.png)

  

•RNN:

Ardından 4 GRU (Geçitli Tekrarlayan Birim) katmanlı bir RNN (Yinelemeli Sinir Ağı) oluşturulmuştur. Optimizasyon algoritması olarak aşırı öğrenmeyi azaltıp daha hızlı ve kararlı öğrenme sağlayan AdamW kullanılmıştır. İlk olarak 4 epoch’a kadar eğitilmiştir. Ardından Early Stopping kullanılmış ve 6. epoch’ta loss arttığı için eğitim durdurulmuştur. Model %89,83 doğrulukla çalışmaktadır. Ancak BERT ile yapılan model daha yüksek doğrulukla çalıştığı için bu modeli kullanılmamıştır.

  

![Modelin Hiperparametreleri](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/rnn.png)

  

![Çeşitli Epoch Değerlerinde RNN Modelinin Doğruluk Değerleri](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/accuracy.png)

  

![Çeşitli Epoch Değerlerinde RNN Modelinin Kayıp Değerleri](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/loss.png)

  

•BERT:

**"bert-base-uncased"**

Ardından BERT ile fine-tuning kullanarak yeni bir model oluşturulmuştur. Bu model ilk olarak 3 epoch ile ardından 5 epoch ile eğitilmiş fakat doğruluğun artmamasından dolayı 3 epoch kullanan model tercih edilmiştir. Optimizasyon algoritması olarak tekrardan AdamW kullanılmıştır. Model’in f1 doğruluğu %91’dir. Fakat BERT-Turkish ile yapılan modelin doğruluğu daha yüksek olduğu için tercih edilmemiştir.

  

![Modelin Değerlendirmesi](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/bert-accuracy.png)

  

![Modelin Hiperparametreleri](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/bert-param.png)

  

•BERT-Turkish:

**"dbmdz/bert-base-turkish-128k-uncased"**

Ardından BERT-Turkish ile fine-tuning kullanarak yeni bir model oluşturuldu. BERT-Turkish, Kemal Oflazer tarafından 128k’lık bir kelime haznesi ile BERT’in üzerine eğitilen bir modeldir. Optimizasyon algoritması olarak tekrardan AdamW kullanılmıştır. Model’in f1 doğruluğu %93’dir. En yüksek doğruluğa sahip model olmasından dolayı uygunsuzluk modeli olarak bu model kullanılmıştır.

  

![Modelin Değerlendirmesi](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/bert-tr-accuracy.png)

  

![Modelin Hiperparametreleri](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/bert-tr-params.png)

  

Bu modellerin doğrulukları aşağıdadır.

  

![Farklı Model Mimarilerinde Uygunsuzluk Modelinin Doğruluk Değerleri](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/offensive-accuracies.png)

  

### Yaş Aralığı Modeli

Yaş aralığı modeli için oluşturulmuş olan veri seti kullanılmıştır. Modeli oluşturmak için çeşitli makine öğrenmesi ve sinir ağı algoritmaları denenmiştir ve aralarında %95,65 ile en yüksek doğruluğa sahip olan Optuna ile optimize edilmiş CatBoost algoritması seçilmiştir. CatBoost, özellikle kategorik verileri otomatik olarak işleyebilmesi sayesinde veri ön işleme sürecini büyük ölçüde kolaylaştıran bir makine öğrenmesi algoritmasıdır. Optuna ise modellerin performansını artırmak için gereken hiperparametrelerin en iyi şekilde ayarlanmasını sağlar.

  

![Modelin Değerlendirmesi](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/catboost-accuracy.jpg)

  

![Modelin Hiperparametreleri](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/catboost-param.jpg)

  

Ayrıca diğer makine öğrenmesi algoritmalarının yüzde kaç doğruluk verdiği aşağıdadır.

  

![Farklı Model Mimarilerinde Uygunsuzluk Modelinin Doğruluk Değerleri](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/accuracies.png)

  

## Okunulabilirlik Puanları

Okunulabilirlik puanları, yapılan araştırmalar sonucu bir metnin farklı dillerde okunulabilirlik endeksini ve farklı yaş aralıkları için okunulabilirlik düzeylerini tespit etmek için oluşturulmuş formüllerdir.

  

Bunlardan en popüler olanları şunlardır:

  

•COE (Çetinkaya Okunulabilirlik Endeksi):

  

$118,823 -(25,987 ∗ASW )-(0,971 ∗AWS)$ (Çetinkaya, 2008)

  

•Ateşman Puanı:

  

$198,825 -40,175 ∗ASW -2,610 ∗AWS$ (Ateşman, 1997)

  

•FRES (Flesch Okunulabilirlik Skoru):

  

$206,835 -(AWS ∗1,015)+(ASW ∗8,46)$ (Flesch, 1948)

  

*AWS = Cümle başına ortalama kelime sayısı

  

*ASW = Kelime başına ortalama hece sayısı

## GUI

customtkinter: Uygulamamıza modern bir görüntü katan özelleştirilmiş tkinter

  

Uygulamamızın iki modu vardır: Gece ve Gündüz modu.

Bu iki modun yaptığı arkaplan ve butonların rengini ayarlamasıdır.

Uygulamamızın sağ alt köşesinde bulunan bilgilendirme butonu, kullanıcının uygulamayı nasıl kullanması gerektiğini ve yapımcısı olan Abra Muhara ekibindeki üyeleri gösterir.

Uygulama ilk açıldığında ortadaki 'Dosya yükle' yazan butona basıldığında bilgisayarımızdan ölçmek istediğimiz kitabı (pdf'yi) seçmemiz istenir.
![Dosya yükleme merkezi](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/dosya_yukle.jpg)

![Kitap Analizi](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/kitap_analiz.jpg)

Dosya seçildikten sonra kitabın gerekli bilgileri toplanır ve bir tablo haline getirilir.

Tablo kullanıcıya sunulur ve önerilen yaş aralığı buna göre bildirilir.

## Proje Yol Haritası

Projede oluşturulan modeller FastAPI, Hugging Face ve Github platformlarına yüklenmiştir. İlerleyen süreçte açık kaynak kodlu olan bu platformlar üzerinden kullanıcılar tarafından geliştirilebilir. Ayrıca proje halk kütüphanelerinde kullanıma sunulabilir.

  

Projede geliştirilebilecek konular şunlardır:

  

•Veri setinde kullanılan kitap sayısı artırılabilir ve daha yüksek doğruluk elde edilebilir.

  

•Ofansif kelime listesindeki kelime sayısı artırılabilir ve daha yüksek doğruluk elde edilebilir.

  

•Uygunsuzluğu ölçen model daha büyük NLP modelleri ile eğitilip daha tutarlı sonuçlar alınabilir.

  

Veri setinde kullanılan kitap sayısının artırılabilmesi için kullanıcıların veri setinde kullanılabilmesi için kitap yükleyebileceği demo bir web sitesi oluşturulmuştur. Bu web sitesinden kullanıcılar farklı kitapları ve bu kitapların yaş aralıklarını yükleyerek veri setini büyütebilir ve daha yüksek doğruluk elde edilmesini sağlayabilir.

  

Web sitesi linki:

https://kitapmetre-veri-seti-araci.glitch.me

  

![KitapMetre Veri Seti Aracı](https://github.com/Abra-Muhara/kitapmetre-2024AcikHackTDDI/blob/main/additionalImages/veri-seti-arac.png)

## Fast-API

Projenin sonunda elde ettiğimiz modelin kullanıcıların daha kolay erişilmesi adına modelimizi Fast-API ile Hugging Face Space ortamına yükledik. Modelleri indirmenize gerek kalmadan (https://abramuhara-fast-api.hf.space) üzerinden istedikleri verileri alabilirler. Sonuçları alma sırasında yapmaları gereken:

1. Uygunsuzluğunu ölçmek istediğiniz bir cümle var ise tek yapmanız gereken (https://abramuhara-fast-api.hf.space/predict/) sayfasına parametreniz {'text': cümle} şeklinde post yapmanızdır. Cevap olarak {'prediction': 0 ise uygun, 1 ise uygun değil} döndürecek.

2. Tabular verilerini elde ettiğiniz kitabınızın yaş aralığını bulmak isterseniz tek yapmanız gereken verilerinizi örnek veri setindeki sütunlar şeklinde sıralamanız ve  (https://abramuhara-fast-api.hf.space/predict-age/) sayfasına parametreniz {'features': list[Float]}
olacak şekilde göndermenizdir. Cevap olarak {"age_group": yazı şeklinde yaş kategorisi} gönderilecektir.
  
## Kurulum Rehberi
Çalıştırmanız tek gereken kod:
```python
pip install -r requirements.txt
```
Sonrasında gui klasöründeki main.py dosyasını çalıştırın

## Kaynakçalar:

ATEŞMAN, Ender. (1997). Türkçe’de okunabilirliğin Ölçülmesi. A.Ü. Tömer Dil Dergisi, sayı:58,s.171-174.

  

Cetinkaya, B. (2008). Türkçe Metinlerde Okunabilirlik Analizi.

  

Flesch, R. (1948). A New Readability Yardstick. Journal of Applied Psychology, 32(3), 221-233. https://doi.org/10.1037/h0057532
