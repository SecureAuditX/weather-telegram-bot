# 🌦️ Telegram Weather Bot

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue?logo=postgresql)](https://www.postgresql.org/)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)](https://core.telegram.org/bots)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> A smart Telegram bot that provides real-time weather updates using the OpenWeatherMap API and stores weather queries in a PostgreSQL database for future insights and analytics.

---

## 📌 Features

- ✅ Get real-time weather for any city by simply messaging the bot
- ✅ Returns temperature and weather condition in human-readable format
- ✅ Saves each query into a PostgreSQL database with timestamp
- ✅ Clean modular Python architecture
- ✅ Easily deployable on cloud platforms like Railway or Fly.io
- ✅ Error-handling for invalid cities and API issues

---

## 🧱 Tech Stack

| Layer          | Technology             |
|----------------|------------------------|
| Programming    | Python 3.10+           |
| Messaging API  | Telegram Bot API       |
| Weather API    | OpenWeatherMap API     |
| Database       | PostgreSQL             |
| Bot Framework  | python-telegram-bot v20+ |
| Hosting        | Railway / Fly.io       |

---

## 🗂️ Project Structure

```bash
weather_bot/
├── telegram_bot.py       # Main Telegram bot logic
├── weather_api.py        # Weather API call logic
├── db.py                 # PostgreSQL DB connection and insertion
├── config.py             # Stores API keys and DB credentials
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Setup Instructions

### 📌 Prerequisites

- Python 3.10+ installed
- Telegram bot token from [@BotFather](https://t.me/BotFather)
- OpenWeatherMap API key from [https://openweathermap.org/api](https://openweathermap.org/api)
- PostgreSQL database (local or cloud)

### 🔧 1. Clone the repository

```bash
git clone https://github.com/SecureAuditX/weather-telegram-bot.git
cd weather-telegram-bot
```

### 🔧 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 🔧 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 🔧 4. Configure your `config.py`

```python
# config.py

TELEGRAM_BOT_TOKEN = "your_telegram_token"
WEATHER_API_KEY = "your_openweathermap_api_key"

DB_NAME = "your_db_name"
DB_USER = "your_db_user"
DB_PASSWORD = "your_db_password"
DB_HOST = "localhost"
DB_PORT = "5432"
```

### 🔧 5. Initialize your PostgreSQL database

Run this SQL manually or inside `init_db()`:

```sql
CREATE TABLE IF NOT EXISTS weather (
    id SERIAL PRIMARY KEY,
    city TEXT,
    temperature REAL,
    condition TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 🚀 Run the bot

```bash
python telegram_bot.py
```

---

## 🌐 Deploy to Railway (Optional)

1. Push your project to GitHub
2. Go to [Railway.app](https://railway.app/)
3. Connect your GitHub repo
4. Add environment variables:
   - `TELEGRAM_BOT_TOKEN`
   - `WEATHER_API_KEY`
   - PostgreSQL credentials
5. Set start command to:

```bash
python telegram_bot.py
```

---

## 🧪 Sample Output

**Telegram:**

```
User: Paris
Bot: 📍 Weather in Paris:
🌡️ 23.4°C
🌤️ scattered clouds
```

**Terminal:**

```
🤖 Bot is running...
✅ Received message: Paris
```

**Database Record:**

| id | city  | temperature | condition        | timestamp           |
|----|-------|-------------|------------------|----------------------|
| 1  | Paris | 23.4        | scattered clouds | 2025-07-12 10:42:00  |

---

## 🙌 Contributing

Contributions are welcome!

1. Fork this repo
2. Create your feature branch (`git checkout -b feature/cool-feature`)
3. Commit your changes (`git commit -m 'Add cool feature'`)
4. Push to the branch (`git push origin feature/cool-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 💡 Ideas for Expansion

- Add weather history retrieval
- User-specific logs
- Weather alerts for extreme conditions
- Multilingual support
- Deploy with webhook instead of polling
- Frontend dashboard (Streamlit or Flask)

---

## ✨ Author

Made with ❤️ by [SecureAuditX](https://github.com/SecureAuditX)
