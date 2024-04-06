from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
import os

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")

default_args = {
    'owner': "Exemple",
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 2,
    'retry_delay': timedelta(minutes=2),
}

@dag(
    dag_id="dag_template_exemple_2",
    max_active_runs=1,
    schedule="0 8 * * *",
    catchup=False,
    description="Dag template exemple",
    default_args=default_args,
    dagrun_timeout=timedelta(minutes=120),
    tags=['exemple', 'jinja', 'template'],
    doc_md="""## Dag exemple
- Dag cocumentation exemple with jinja template
"""
)
def template_exemple():

    start = EmptyOperator(task_id="start")

    bq_job_task1 = BigQueryInsertJobOperator(
        task_id=f"task_table_exemple",
        location=LOCATION,
        project_id=PROJECT_ID,
        configuration={
            "query": {
                "query": f"SELECT * FROM {PROJECT_ID}.dag_exemple_bq.table_exemple",
                "useLegacySql": False,
                "priority": "BATCH",
            }
        },
    )

    bq_job_task2 = BigQueryInsertJobOperator(
        task_id=f"task_table_exemple_2",
        location=LOCATION,
        project_id=PROJECT_ID,
        configuration={
            "query": {
                "query": f"SELECT * FROM {PROJECT_ID}.dag_exemple_bq_2.table_exemple_2",
                "useLegacySql": False,
                "priority": "BATCH",
            }
        },
    )

    end = EmptyOperator(task_id="end")
        
    start >> [bq_job_task1, bq_job_task2] >> end