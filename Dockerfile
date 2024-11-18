FROM apache/airflow:2.4.3

USER root

RUN python3 --version

RUN apt-get update && apt-get install -y \
    curl \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

USER airflow

RUN pip install --upgrade pip
RUN pip install poetry

RUN mkdir /home/airflow/project

COPY --chown=airflow:airflow . /home/airflow/project/

WORKDIR /home/airflow/project
RUN poetry install --no-dev

USER airflow