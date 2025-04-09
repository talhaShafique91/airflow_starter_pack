# Airflow Starter Pack 🚀

This starter pack helps you get up and running with a production-ready Apache Airflow setup in minutes — with built-in retry logic, Slack & Gmail alerting, timeout handling, and a Dockerized dev environment.

---

## 📦 What’s Included

- ✅ A sample Airflow DAG (`etl_airflow_starter_pack.py`) with:
  - Retry logic
  - Task execution timeout
  - Slack alert on failure
  - Gmail email alert on failure
- 🐳 Docker + Docker Compose setup
- 🔐 `.env` file-based config (Gmail SMTP, Slack webhook, etc.)
- 🧪 Dummy ETL task for quick testing
- 🧱 Clean project structure

---

## 🚀 Quick Start

1. **Clone this repo**

```bash
git clone https://github.com/talhaShafique91/airflow_starter_pack.git
cd airflow_starter_pack
```

2. **Create .env file**
```bash
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=you@gmail.com
SMTP_PASSWORD=your_gmail_app_password
SMTP_MAIL_FROM=you@gmail.com
```

3. **Build and start Airflow**
```bash
docker-compose up --build
```

4. **Access Airflow UI**
```bash
Open http://localhost:8080

Login: airflow / airflow
```
5. **Trigger the DAG**
```bash
Manually trigger the DAG etl_airflow_starter_pack

Use failure simulation to test retries, alerts, and timeout
```