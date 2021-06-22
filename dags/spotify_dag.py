from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from spotify_etl import run_spotify_etl

default_args = {
    "owner": "airflow",
    "depends_on_path": False,
    "start_date": days_ago(2021, 6, 10),
    "email": ["leonardovselan@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "delay_on_retry": timedelta(minutes=1)
}

dag = DAG(
    "spotify_dag",
    default_args=default_args,
    description="Primeira DAG com processo de ETL!",
    schedule_interval=timedelta(days=1)
)

run_etl = PythonOperator(
    task_id="whole_spotify_etl",
    python_callable=run_spotify_etl,
    dag=dag
)

run_etl
