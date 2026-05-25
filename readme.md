# Telegram WebApp Launcher Bot

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge\&logo=python)
![Aiogram](https://img.shields.io/badge/Aiogram-3.26.0-2CA5E0?style=for-the-badge\&logo=telegram)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Telegram-black?style=for-the-badge\&logo=telegram)

A modern Telegram bot built with `Aiogram 3`, designed to send Web Apps and Telegram Channels using inline buttons.

The project is structured for scalability and future expansion, including:

* Admin panel
* Bot settings management
* Channel & group management
* WebApp configuration
* User management

---

# Features

* Telegram WebApp integration
* Inline keyboard support
* Channel promotion buttons
* Clean project architecture
* Middleware support
* Admin handlers
* Logging system
* Environment-based configuration
* Ready for VPS deployment

---

# Tech Stack

* Python 3.12
* Aiogram 3.26.0
* Pydantic Settings 2.13.1

---

# Project Structure

```bash
.
├── core/
│   ├── config.py
│   └── logger.py
│
├── handlers/
│   ├── admin.py
│   ├── clean_chat.py
│   └── user.py
│
├── keyboards/
│   ├── admin_menu.py
│   └── user_menu.py
│
├── middlewares/
│   └── who.py
│
├── states/
│
├── logs/
│   └── bot.log
│
├── .env
├── .env.example
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

## Clone repository

```bash
git clone https://github.com/yourusername/telegram-webapp-bot.git
cd telegram-webapp-bot
```

## Create virtual environment

```bash
python -m venv venv
```

## Activate virtual environment

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env` file:

```env
BOT_TOKEN=your_bot_token_here

TG_ADMIN_IDS=[123456789,987654321]

WEB_APP_URL=https://yourwebapp.com

CHANNEL_URL=https://t.me/yourchannel
```

---

# Run Bot

```bash
python main.py
```

---

# Deployment

Recommended deployment environment:

* VPS (Ubuntu 22.04+)
* Systemd service
* Nginx (optional)
* Docker support (planned)

---

# Roadmap

* [x] WebApp button support
* [x] Channel inline buttons
* [x] Middleware system
* [ ] Admin panel
* [ ] Dynamic bot settings
* [ ] Group management
* [ ] Channel management
* [ ] Web dashboard
* [ ] Database integration
* [ ] Docker support
* [ ] CI/CD pipeline

---

# License

This project is licensed under the MIT License.

---


---

# Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss what you would like to change.

---

# Author

[![GitHub](https://img.shields.io/badge/GitHub-jorabeknazarmatov-181717?style=for-the-badge&logo=github)](https://github.com/jorabeknazarmatov)
