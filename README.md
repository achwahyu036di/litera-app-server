# 📦 Project Setup Guide

Panduan ini menjelaskan cara mengatur lingkungan virtual Python dan menginstal semua dependensi yang dibutuhkan proyek menggunakan `requirements.txt`.

## 📁 Prasyarat

Pastikan Anda sudah menginstal:
- Python 3.6+ (direkomendasikan Python 3.10+)
- pip (biasanya sudah termasuk dalam Python)
- `virtualenv` (opsional jika tidak menggunakan `venv` bawaan Python)

Cek versi Python dan pip:

```bash
python --version
pip --version
```

## Langkah Setup
#### Clone Repository
```bash
git clone https://github.com/Fiyanz/litera-app-server.git
cd litera-app-server
```
#### Buat Virtual Environment
```bash
# Untuk Linux/MacOS
python3 -m venv venv

# Untuk Windows
python -m venv venv
```
#### Aktifkan Virtual Environment
```bash
# Linux/MacOS
source venv/bin/activate

# Windows (Command Prompt)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1
```
#### Install Dependencies
```bash
pip install -r requirements.txt
```
#### Run Program
```bash
fastapi dev app.py
```
