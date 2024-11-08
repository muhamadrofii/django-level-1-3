

# Latihan Model Form

## Model

Mmodel bernama `Customer` dengan field sebagai berikut:

- **First Name**: Menyimpan nama depan customer.
- **Last Name**: Menyimpan nama belakang customer.
- **Email**: Menyimpan alamat email customer.

## Instalasi

1. **Clone repository ini**:

   ```bash
   git clone https://github.com/muhamadrofii/django-level-1-3

   cd firstproject
   ```

2. **Buat virtual environment** (Opsional tetapi disarankan):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Linux/macOS
   venv\Scripts\activate     # Untuk Windows
   ```

3. **Install dependensi**:

   Pastikan Anda memiliki Django terinstal. Jika belum, Anda dapat menginstalnya dengan perintah:

   ```bash
   pip install django
   ```

   Kemudian, install dependensi lainnya:

   ```bash
   pip install -r requirements.txt
   ```

4. **Menjalankan server Django**:

   Setelah semua dependensi terinstal, jalankan server Django:

   ```bash
   python manage.py runserver
   ```

5. **Akses aplikasi**:

   Buka browser dan akses aplikasi di `http://127.0.0.1:8000/`

   `/index` Untuk halaman awal

   `/admin` Untuk administrator

   `/subscribe`Untuk form subscribe

## Migrasi Database

Untuk membuat dan mengupdate database sesuai dengan model `Customer`, jalankan perintah berikut:

```bash
python manage.py makemigrations
python manage.py migrate
```