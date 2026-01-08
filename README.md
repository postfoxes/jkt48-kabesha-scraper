# 🎤 JKT48 Kabesha Scraper

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/)

**JKT48 Kabesha Scraper** adalah alat otomatisasi berbasis Python yang dirancang untuk mengunduh seluruh foto profil resmi (*Kabesha*) member JKT48 langsung dari situs web resmi. Proyek ini menggabungkan teknik *web scraping* tingkat lanjut dengan pemrograman asinkron untuk memberikan performa pengunduhan yang maksimal.

---

## ✨ Fitur Utama

* **⚡ High-Speed Asynchronous Downloading**: Menggunakan `httpx` dan `asyncio` untuk mengunduh puluhan gambar secara simultan dalam hitungan detik.
* **🛡️ Bot Detection Bypass**: Terintegrasi dengan `curl_cffi` (Impersonate Chrome) untuk melewati proteksi TLS/WAF yang mungkin memblokir permintaan *scraping* standar.
* **📂 Auto-Organization**: Secara otomatis membuat direktori penyimpanan dan menamai file secara rapi berdasarkan nama member yang diekstrak dari URL.
* **🚦 Concurrency Control**: Menggunakan *Semaphore* untuk membatasi jumlah koneksi aktif, memastikan proses berjalan stabil tanpa membebani server tujuan.
* **🔍 Clean Data Extraction**: Menggunakan `BeautifulSoup4` untuk memparsing struktur HTML situs JKT48 secara akurat.

---

## 🛠️ Teknologi yang Digunakan

| Library | Kegunaan |
| :--- | :--- |
| **`curl_cffi`** | Meniru *browser fingerprint* (Chrome) untuk menghindari deteksi bot. |
| **`BeautifulSoup4`** | Mengekstrak data dan URL gambar dari struktur HTML. |
| **`httpx`** | Melakukan permintaan HTTP secara asinkron (Async HTTP Client). |
| **`asyncio`** | Mengelola *event loop* untuk eksekusi tugas paralel secara efisien. |

---

## 🚀 Cara Memulai

### Prasyarat
Pastikan Anda sudah menginstal Python 3.8 atau versi yang lebih baru di sistem Anda.

### Instalasi
1.  **Clone repositori ini:**
    ```bash
    git clone [https://github.com/username/jkt48-kabesha-scraper.git](https://github.com/username/jkt48-kabesha-scraper.git)
    cd jkt48-kabesha-scraper
    ```

2.  **Instal dependensi yang diperlukan:**
    ```bash
    pip install httpx curl_cffi beautifulsoup4
    ```

### Penggunaan
Jalankan script utama untuk memulai proses pengunduhan otomatis:
```bash
python scrape_jkt48.py
