import json
from collections import defaultdict

def extract_journal_with_most_drugs(json_file):
    """Extract the journal with the most unique drugs mentioned."""
    with open(json_file, 'r') as f:
        data = json.load(f)

    journal_drug_count = defaultdict(set)

    for drug, details in data['drugs'].items():
        for mention in details.get('pubmed_mentions', []):
            journal = mention.get('journal')
            if journal:
                journal_drug_count[journal].add(drug)

        for trial in details.get('clinical_trials', []):
            journal = trial.get('journal')
            if journal:
                journal_drug_count[journal].add(drug)

    max_journal = max(journal_drug_count, key=lambda k: len(journal_drug_count[k]), default=None)
    max_count = len(journal_drug_count[max_journal]) if max_journal else 0

    print(f"Journal with the most drugs: {max_journal} with {max_count} drugs.")