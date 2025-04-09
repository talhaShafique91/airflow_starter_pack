Airflow Starter Pack 🚀
This starter pack helps you get up and running with a production-ready Apache Airflow setup in minutes — with built-in retry logic, Slack & Gmail alerting, timeout handling, and a Dockerized dev environment.

✅ What’s Included
Sample Airflow DAG with:

Retry logic

Task execution timeout

Slack alert on failure

Gmail email alert on failure

Docker + Docker Compose environment

.env-based secure config (for Gmail + Slack)

Dummy ETL task for testing failure scenarios

Works out-of-the-box in under 10 minutes

🚀 Quick Start
Clone this repo
git clone https://github.com/talhaShafique91/airflow_starter_pack.git
cd airflow_starter_pack

Create a .env file with the following content:

SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=you@gmail.com
SMTP_PASSWORD=your_gmail_app_password
SMTP_MAIL_FROM=you@gmail.com

Start the Airflow environment
docker-compose up --build

Login to Airflow UI
Visit: http://localhost:8080
Username: airflow
Password: airflow

Trigger the DAG
Test Slack alerts, email alerts, timeout, and retry logic by raising a failure in the dummy ETL task.

🧪 How to Test Features
Raise an exception in the task to test retries and alerts

Add time.sleep(4000) to test execution timeout

Add Slack webhook in Airflow Variables (slack_webhook)

Use Gmail App Password to test email alerts

👥 Who Is This For?
Data engineers setting up Airflow from scratch

Startups that want built-in alerting and monitoring

Engineers who need a clean, working example to build from

📬 Support
Open an issue or reach out on LinkedIn: https://linkedin.com/in/talhashafique
Email: youremail@domain.com

🔥 Coming Soon
Setup walkthrough video

Gumroad product bundle

Advanced version with DBT, Airbyte & CI/CD

Built with ❤️ by @talhaShafique91