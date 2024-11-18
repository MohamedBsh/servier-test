from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from servier.src.pipeline import run_data_pipeline

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

dag = DAG(
    'data_pipeline_dag',
    default_args=default_args,
    schedule_interval='@daily',
    description='A DAG to run the Servier data processing pipeline daily.'
)

generate_drug_graph = PythonOperator(
    task_id='generate_drug_graph',
    python_callable=run_data_pipeline,
    dag=dag
)