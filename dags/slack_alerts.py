import requests
from airflow.models import Variable

def slack_alert(context):
    dag_id = context.get('dag').dag_id
    task_id = context.get('task_instance').task_id
    log_url = context.get('task_instance').log_url
    message = f":red_circle: DAG *{dag_id}* failed on task *{task_id}*. <{log_url}|View Logs>"

    webhook_url = Variable.get("slack_webhook")
    requests.post(webhook_url, json={"text": message})
