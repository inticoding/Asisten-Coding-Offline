# 🧠 AI Coding & Debugging Assistant (Offline Mode)

AI Asisten Coding & Debugging lokal berbasis model CodeLlama (tanpa internet) yang membantu kamu memahami, memperbaiki, dan meningkatkan kode secara offline.

## ✨ Fitur

- 💬 Interaktif dengan antarmuka chat
- 🧑‍💻 Membantu debugging & perbaikan kode
- ⚙️ Dapat digunakan 100% offline (tanpa internet)
- 🧠 Menggunakan model lokal seperti codellama:7b via Ollama
- 📜 Menyimpan riwayat percakapan antar sesi

## 📦 Instalasi

1. Clone repositori ini

```
git clone https://github.com/namamu/ai-coding-debug-assistant-offline.git
cd ai-coding-debug-assistant-offline
```

2. Install dependensi Python

Disarankan menggunakan virtual environment.

```
pip install -r requirements.txt
```

3. Install dan jalankan Ollama

Download Ollama dari https://ollama.com dan install sesuai OS kamu (Linux/Windows/macOS).

## 📜 Buat requirements.txt

4. Pull model CodeLlama (atau model coding lain)

```
ollama pull codellama:7b
```

> 💡 Kamu juga bisa gunakan model seperti deepseek-coder:6.7b atau phind:latest sesuai kebutuhan.

## 🚀 Menjalankan Aplikasi

```
streamlit run app.py
```

## 📋 Contoh Penggunaan

```
💬 Pengguna: Apa bug dari kode Python ini?

def add(a, b):
return a + b

💡 AI Assistant:
Indentasi pada `return` salah. Seharusnya:
    
def add(a, b):
    return a + b
```

## 🧠 Model yang Didukung

| Nama Model     | Cocok Untuk            |
| -------------- | ---------------------- |
| codellama:7b   | Debugging & Penjelasan |
| deepseek-coder | Analisis & Refactoring |
| phind\:latest  | Chat Coding Umum       |

> Pastikan kamu sudah pull model dari Ollama sebelum digunakan.

# 📲 Ingin update tips coding, AI tools, dan teknologi terbaru lainnya?

Follow kami di sosial media:

👉 Instagram: @inticoding  
👉 TikTok: @inticoding  
👉 Threads: @inticoding  

# Jangan lewatkan konten menarik lainnya! 🚀💻