from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
from slack_alerts import slack_alert  # ✅ Updated import

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 3,
    'retry_delay': timedelta(minutes=1),
    'email_on_failure': True,
    'email': ['abc@example.com'],
    'execution_timeout': timedelta(seconds=60),
    'on_failure_callback': slack_alert
}

def dummy_etl(**kwargs):
    print("Running ETL job...")
    # raise Exception("Simulated failure to test retry logic")

with DAG(
    dag_id='etl_airflow_starter_pack',
    default_args=default_args,
    description='A starter DAG for ETL with retries and alerts',
    schedule_interval='@daily',
    catchup=False
) as dag:
    run_etl = PythonOperator(
        task_id='run_etl_task',
        python_callable=dummy_etl
    )

    run_etl
