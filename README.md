<!-- README ini dihasilkan otomatis oleh .github/workflows/generate-readme.yml -->
<!-- Jangan edit manual: perubahan akan ditimpa pada run berikutnya. -->

<h1 align="center">🤖 Bot Collection 👋</h1>

<p align="center">
  <a href="https://github.com/antono4/bot"><img alt="GitHub repo" src="https://img.shields.io/badge/GitHub-antono4/bot-blue?logo=github"></a>
  <a href="https://antono4.github.io/bot/"><img alt="Live Demo" src="https://img.shields.io/badge/Live%20Demo-Online-success?logo=githubpages"></a>
  <img alt="Files" src="https://img.shields.io/badge/Files-50-informational">
  <img alt="Last commit" src="https://img.shields.io/github/last-commit/antono4/bot">
</p>

---

## 📖 Tentang

Repository **`bot`** adalah situs statis yang dibangun dengan HTML, Python.
Situs ini diterbitkan melalui **GitHub Pages** dan dapat diakses di [`https://antono4.github.io/bot/`](https://antono4.github.io/bot/).

## 🗂️ Struktur Proyek

```
bot/
.github/
  workflows/
DOCUMENTATION-COMPLETE.html
DOCUMENTATION-COMPLETE.md
DOCUMENTATION-COMPLETE.pdf
DOCUMENTATION.md
DOCUMENTATION.pdf
LICENSE
agent-os/
  README.md
  index.html
  requirements.txt
  server.py
agent-windows/
  .env.example
  README.md
  agent.py
  bot/
  config.py
  requirements.txt
bot-ecommerce/
  .env.example
  README.md
  requirements.txt
  shopify_bot.py
  woocommerce_bot.py
bot-openhands/
  README.md
  agent_bot.py
  config.yaml
  requirements.txt
bot-scraping/
  README.md
  config.yaml
  requirements.txt
  scraper.py
bot-social-media/
  .env.example
  README.md
  discord_bot.py
  requirements.txt
  telegram_bot.py
  twitter_bot.py
bot-support/
  .env.example
  README.md
  requirements.txt
  ticket_bot.py
bot-trading/
  README.md
  config.example.yaml
  main.py
  requirements.txt
index.html
```

## 🌐 Sub-Proyek / Demo

Repository ini juga memuat sub-proyek (masing-masing punya `index.html` tersendiri):

| Folder | Keterangan |
|--------|-----------|
| [`agent-os`](./agent-os) | Agent OS - AI Agent dengan Web Interface |

## 🛠️ Teknologi

Berdasarkan ekstensi berkas yang terdeteksi di repository:

- `HTML`
- `Python`

> Total **50 berkas** di repository (di luar `.git`, `node_modules`, `dist`, dan `build`).

## 🚀 Menjalankan Secara Lokal

Tanpa dependency apa pun. Buka `index.html` langsung di browser, atau jalankan server statis:

```bash
python3 -m http.server 8000
# lalu buka http://localhost:8000
```

## 📬 Kontak

- GitHub: [antono4](https://github.com/antono4)

## 📄 Lisensi

Proyek ini dilisensikan di bawah MIT License — lihat berkas [`LICENSE`](./LICENSE).

---

<sub>README ini di-generate otomatis oleh GitHub Actions `.github/workflows/generate-readme.yml`.</sub>
