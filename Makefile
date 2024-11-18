.PHONY: build init_docker test run_manual_dag clean find_top_journal get_output install-dev test up up-d status

JSON_FILE ?= servier/data/drug_mentions_graph.json

build:
	docker build .

init_docker:
	docker-compose down --volumes --remove-orphans
	docker-compose build --no-cache
	docker-compose up -d

up:
	docker-compose up

up-d:
	docker-compose up -d

status:
	docker-compose ps

run_manual_dag:
	docker-compose run airflow-scheduler airflow dags trigger dag

clean:
	docker-compose down --volumes --remove-orphans
	rm -rf dist build *.egg-info

test:
	pytest tests

find_top_journal:
	python3 -c "from journal_drug_extractor import extract_journal_with_most_drugs; extract_journal_with_most_drugs('$(JSON_FILE)')"

get_output:
	python3 -c "import json; print(json.dumps(json.load(open('$(JSON_FILE)')), indent=2))"