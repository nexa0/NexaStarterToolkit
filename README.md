# Nexa Basic Toolkit v1.0

A lightweight terminal-based collection of beginner-friendly security, networking, and utility tools.

## Features

- Hash format checker
- File hashing: MD5, SHA-1, SHA-256, SHA-512
- Password strength estimator
- Base64 encoder/decoder
- IP information lookup
- HTTP status and response information
- Basic TCP port checker
- Image EXIF metadata viewer
- Colorized terminal interface
- Modular Python structure

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/Nexa-Basic-Toolkit.git
cd Nexa-Basic-Toolkit
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

## Project Structure

```text
Nexa-Basic-Toolkit/
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── core/
│   ├── banner.py
│   └── utils.py
└── tools/
    ├── hash_checker.py
    ├── file_hasher.py
    ├── password_strength.py
    ├── base64_tool.py
    ├── ip_info.py
    ├── http_status.py
    ├── port_checker.py
    └── metadata_viewer.py
```

## Responsible Use

This project is intended for learning, defensive security, personal systems, and authorized labs.

Only use network features against systems you own or have explicit permission to test.

## Version

`1.0.0`
