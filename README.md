# **Kalkulator Berbasis AI dengan Python dan Replicate**

Ini adalah proyek kalkulator web yang menunjukkan integrasi antara **front-end** (HTML/CSS/JavaScript) dan **back-end** (Python Flask) untuk melakukan perhitungan menggunakan model AI. Kalkulator ini tidak hanya menghitung operasi dasar, tetapi juga menggunakan **Granite Model** dari IBM yang diakses melalui Replicate.

## **Cara Kerja**

Proyek ini menggunakan arsitektur full-stack:

* **Front-end (index.html)**: Menyediakan antarmuka grafis kalkulator. Mengumpulkan ekspresi matematika dari pengguna dan mengirimkannya ke back-end.  
* **Back-end (app.py)**: Bertindak sebagai API server. Menerima ekspresi dari front-end, mengirimkannya ke model **Granite** di Replicate, dan mengembalikan hasilnya.

## **Persyaratan**

Pastikan Anda memiliki hal-hal berikut terinstal di komputer Anda:

* **Python 3.x**  
* **pip** (manajer paket Python)

## **Instalasi**

1. **Instal library Python yang diperlukan**:  
   pip install Flask Flask-Cors replicate

2. **Dapatkan Kunci API Replicate Anda**:  
   * Daftar atau masuk ke [situs web Replicate](https://replicate.com).  
   * Buka halaman "API Tokens" di pengaturan akun Anda.  
   * Salin kunci API Anda.  
3. **Siapkan Variabel Lingkungan**:  
   * **PENTING**: Jangan pernah menaruh kunci API Anda langsung di dalam kode.  
   * Di terminal atau Command Prompt, atur variabel lingkungan dengan kunci API Anda.

Untuk macOS/Linux:export REPLICATE\_API\_TOKEN="\[kunci\_api\_anda\]"  
Untuk Windows:set REPLICATE\_API\_TOKEN="\[kunci\_api\_anda\]"

## **Cara Menjalankan Aplikasi**

1. **Jalankan server back-end**:  
   * Di terminal, navigasi ke direktori proyek Anda.  
   * Jalankan server Flask:

python app.py  
Anda akan melihat pesan yang menunjukkan bahwa server berjalan di http://127.0.0.1:5000.

2. **Buka kalkulator di browser**:  
   * Buka file index.html di browser web favorit Anda.

Sekarang, setiap kali Anda melakukan perhitungan, ia akan diproses oleh model AI dan hasilnya akan dikembalikan ke kalkulator.