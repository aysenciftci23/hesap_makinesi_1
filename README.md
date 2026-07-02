# 🧮 Gelişmiş Bilimsel Hesap Makinesi

Modern, yüksek kontrastlı ve estetik ("Clean Girl" konseptli) kullanıcı arayüzüne sahip, Python ve Tkinter ile geliştirilmiş gelişmiş bir hesap makinesi projesidir. Proje, "Frontend" (Önyüz) ve "Backend" (Arka plan) mimarisinin birbirinden ayrılarak takım çalışmasıyla birleştirildiği modüler bir yapıya sahiptir.

🔗 **Proje Bağlantısı:** [hesap_makinesi_1](https://github.com/aysenciftci23/hesap_makinesi_1)

---

## ✨ Özellikler

* **Temel Matematik İşlemleri:** Toplama, çıkarma, çarpma ve bölme.
* **Bilimsel Fonksiyonlar:** Trigonometri (`sin`, `cos`, `tan`, `cot`, `asin`, `acos`, `atan`), Logaritma (`log`, `ln`), Karekök (`√`), Üs alma (`^`), Modülüs (`%`) ve Faktöriyel (`!`).
* **Derece / Radyan Modu:** Trigonometrik hesaplamalar için tek tuşla mod değiştirme (`Deg/Rad`).
* **Klavye Entegrasyonu:** Hızlı kullanım için klavye kısayolları:
    * `Enter` ➔ Eşittir (Hesapla)
    * `Backspace` ➔ Son karakteri sil
    * `Escape (Esc)` ➔ Ekranı tamamen temizle (C)
* **Modern ve Şık Arayüz (UI):** Göz yormayan, yüksek kontrastlı pastel lila ve koyu mürdüm tonlarından oluşan özel renk paleti.
* **Akıllı Metin Ayrıştırma (Parsing):** Kullanıcının girdiği karmaşık işlemleri ve parantez önceliklerini arka planda güvenle çözümleyen sistem.

---

## 📂 Proje Yapısı

Proje, görev dağılımı yapılarak geliştirilmiş bağımsız modüllerden oluşmaktadır:

* **`UI.py`:** Kullanıcı arayüzü katmanı. Tkinter kullanılarak tasarlandı. Kullanıcı girdilerini yakalar, gerekli formatlamaları yapar (örn. çıkarma ve modülüs işlemleri için frontend yamaları) ve arka plan motoruna iletir.
* **`temel.py`:** Temel matematiksel işlemlerin ve metin ayrıştırma (parsing) algoritmalarının (`hesapla_ifade`) bulunduğu ana hesaplama motoru.
* **`bilimsel.py`:** İleri düzey matematiksel ve trigonometrik işlemlerin yer aldığı fonksiyon kütüphanesi.
* **`test_temel.py`:** Uygulama mantığının %100 doğrulukla çalıştığını garanti altına alan `pytest` altyapılı otomatik test dosyası.

---

## 🚀 Kurulum ve Kullanım

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. **Repoyu Klonlayın:**
   ```bash
   git clone [https://github.com/aysenciftci23/hesap_makinesi_1.git](https://github.com/aysenciftci23/hesap_makinesi_1.git)
