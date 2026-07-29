# Windows Agent - AI Automation untuk Windows 11

Agent AI yang berjalan di Windows 11.

## Fitur

- AI Chat dengan GPT-4/Claude
- File Operations (baca, tulis, list file)
- Web Search (cari di internet)
- Python Code Execution
- Windows Automation (mouse, keyboard, screenshot)

## Requirements

- Windows 11
- Python 3.10+
- OpenAI API Key

## Quick Start

```powershell
cd agent-windows
pip install -r requirements.txt
copy .env.example .env
# Edit .env dan masukkan API key
python agent.py
```

## Commands

- `baca file <path>` - Baca file
- `tulis file <path> | <content>` - Tulis file
- `list file <path>` - List file di folder
- `cari <query>` - Cari di web
- `jalankan <kode>` - Jalankan kode Python

## License: MIT
