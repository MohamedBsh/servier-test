import os

class Config:
    DATA_DIR = os.getenv('DATA_DIR', 'servier/data/')
    CLINICAL_TRIALS_FILE = os.path.join(DATA_DIR, 'clinical_trials.csv')
    DRUGS_FILE = os.path.join(DATA_DIR, 'drugs.csv')
    PUBMED_CSV_FILE = os.path.join(DATA_DIR, 'pubmed.csv')
    PUBMED_JSON_FILE = os.path.join(DATA_DIR, 'pubmed.json')