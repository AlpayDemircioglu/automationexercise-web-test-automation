# AutomationExercise Web Test Otomasyonu

Bu proje, **AutomationExercise** web sitesinin temel kullanıcı senaryolarını test etmek amacıyla **Python, Selenium ve Pytest** kullanılarak hazırlanmıştır.

🔗 Test edilen site: https://automationexercise.com/

---

## 🧪 Projenin Amacı

Bu projenin amacı bir e-ticaret sitesinin temel fonksiyonlarını otomasyon testleri ile doğrulamaktır.  
Özellikle aşağıdaki senaryolara odaklanılmıştır:

- Login (Giriş) işlemleri
- Register (Kayıt) sayfası işlemleri
- Sayfa linklerinin doğrulanması
- Temel navigasyon ve UI kontrolleri

Bu proje, **Software QA / Test Otomasyonu** alanındaki öğrenme sürecimin bir parçası olarak geliştirilmiştir.

---

## 🛠 Kullanılan Teknolojiler

- Python  
- Selenium WebDriver  
- Pytest  
- ChromeDriver  
- CSS Selector ve XPath

---



## 🧩 Framework Yapısı

- **pages** klasörü altında sayfalara ait locator ve fonksiyonlar bulunmaktadır
- **tests** klasörü altında test senaryoları yer almaktadır
- `conftest.py` dosyası WebDriver kurulumunu ve test konfigürasyonunu sağlar
- Okunabilirliği artırmak için **basit ve sade bir Page Object yapısı** kullanılmıştır

> ⚠️ Not:  
> Bu projede **ileri seviye bir framework yapısı hedeflenmemiştir**.  
> Amaç, Selenium ve Pytest mantığını öğrenmek ve test senaryoları yazma pratiği kazanmaktır.

---
## 🎯 Projenin Hedefi

- Selenium ile test otomasyonu becerilerini geliştirmek

- Pytest yapısını daha iyi anlamak

- Okunabilir ve sürdürülebilir testler yazmak

- GitHub üzerinde gerçek projeler paylaşmak