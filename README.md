#SmartGuard Sensor System

Bu projenin temel amacı, ev ortamında sensörler aracılığıyla sıcaklık, ışık ve su seviyelerini ölçerek, belirlenen eşik değerleri aşıldığında kullanıcıyı uyarmak ve gerekli önlemlerin alınmasını sağlamaktır.
##Proje Açıklaması

Bu projede Arduino kullanılarak ortamın sıcaklık, ışık ve su seviyesi değerleri; DHT11 (sıcaklık–nem sensörü), LDR (ışık sensörü) ve su seviye sensörü aracılığıyla ölçülmüştür. Toplanan veriler Python üzerinden bilgisayara aktarılmış, pandas ve matplotlib kütüphaneleri kullanılarak analiz edilmiş ve çeşitli grafiklerle görselleştirilmiştir.
Belirli eşik değerlerinin aşılması durumunda oluşan alarm olayları kaydedilmiş ve bu uyarıların dağılımı pasta grafiği ile gösterilmiştir. Ayrıca veriler günlük olarak CSV dosyalarına kaydedilerek arşivlenmiştir.
Projede kullanılan RTC (Real Time Clock) modülü sayesinde anlık saat bilgisi okunmuş ve her veri kaydına zaman damgası eklenmiştir. Bunun yanında, LCD I2C ekran üzerinden sensör verileri ile birlikte tarih ve saat bilgileri gerçek zamanlı olarak görüntülenmiştir.
Sistemin genel durumunu değerlendirebilmek amacıyla, elde edilen sensör ölçümlerinin ortalama değerleri de hesaplanarak raporlanmıştır.
##Kullanılan Teknolojiler

Donanım:Arduino Uno, breadboard, buzzer, RGB LED, üç adet 220 ohm direnç, bir adet 10k direnç, DHT11 sensörü, LDR, su seviye sensörü, RTC modülü, LCD I2C ekran ve jumper kablolar.
Yazılım:Arduino IDE, Python.
Python Kütüphaneleri:serial,time,pandas,matplotlib,os,datetime.
# Kurulum ve Kullanım
## Yapım Aşaması
Devreyi Kurun: Board üzerine belirtilen devre elemanlarını şemaya uygun bir şekilde yerleştirin ve bağlantıları yapın.
Gerekli Kütüphaneleri Kurun: Python için pyserial kütüphanesini terminal üzerinden pip install pyserial komutu ile yükleyin.
Kodları Hazırlayın: Proje için gerekli olan hem Arduino hem de Python kodlarını yazın.
## Uygulama Aşaması
Donanımı Hazırlayın: Devreyi kurduktan sonra Arduino kartınızı USB kablosu ile bilgisayara bağlayın.
Arduino Kodunu Yükleyin: Arduino IDE'sinden kodu derleyin ve kartınıza yükleyin. Yükleme tamamlandıktan sonra Arduino IDE'sini kapatın.
Python Kodunu Çalıştırın: COM port numarasını kendi kartınıza uygun şekilde ayarladıktan sonra, Python dosyasını çalıştırın.
##Devre Bağlantıları
-LDR Sensörü
Bir bacağı breadboard’un + hattına bağlandı.
Diğer bacağına 10k direnç ve jumper kablo bağlandı.
Jumper kablonun ucu A0 pinine, direncin boşta kalan ucu – hattına bağlandı.
-DHT11 Sensörü
Signal pini → D6
VCC ve GND → Breadboard + ve – hatları
-Buzzer
Bir bacağı D7 pinine,
Diğer bacağı – hattına bağlandı.
-RGB LED Modülü
R, G, B pinlerine sırasıyla 220 ohm dirençler bağlandı.
Dirençlerin diğer uçları D8, D9 ve D10 pinlerine bağlandı.
LED’in ortak katodu – hattına bağlandı.
-Su Seviye Sensörü
Signal pini → A2
VCC ve GND → + ve – hatları
-RTC Modülü
VCC → +, GND → –
CLK → D11, DAT → D12, RST → D13
LCD I2C Ekran
SDA → A4, SCL → A5
VCC ve GND → + ve – hatları
##Devrenin Fotoğrafı
![WhatsApp Image 2025-11-23 at 22 53 04](https://github.com/user-attachments/assets/7d61e418-d759-42ae-b821-9d938fa8eac3)
