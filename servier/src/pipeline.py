from cleaner import DataCleaner
from merger import merge_data
from graph_builder import build_data_graph, save_graph_to_json
from loader import DataLoader
from config import Config
import pandas as pd
from typing import List, Dict, Any

def drug_mentions(df: pd.DataFrame, drugs: pd.DataFrame, data_type: str) -> List[Dict[str, Any]]:
    """
    Extracts drug mentions from the given DataFrame based on the specified data type.

    Args:
        df (pd.DataFrame): The DataFrame containing mentions (clinical trials or PubMed).
        drugs (pd.DataFrame): The DataFrame containing drug information.
        data_type (str): The type of data to process ('clinical_trials' or 'pubmed').

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing drug mentions.
    """
    mentions = []
    for _, drug_row in drugs.iterrows():
        drug_name = drug_row['drug']
        for _, row in df.iterrows():
            if data_type == 'clinical_trials':
                if 'scientific_title' in row and drug_name.lower() in row['scientific_title'].lower():
                    mentions.append({
                        "id": row['id'],
                        "title": row['scientific_title'],
                        "journal": row['journal'],
                        "date": row['date'],
                        "drug": drug_name
                    })
            elif data_type == 'pubmed':
                if 'title' in row and drug_name.lower() in row['title'].lower():
                    mentions.append({
                        "id": row['id'],
                        "title": row['title'],
                        "journal": row['journal'],
                        "date": row['date'],
                        "drug": drug_name
                    })
    return mentions

def run_data_pipeline() -> None:
    """
    Executes the data pipeline to load, clean, and process drug mentions,
    and then saves the resulting graph to a JSON file.
    """
    config = Config()
    data_loader = DataLoader(config)

    clinical_trials = data_loader.load_clinical_trials()
    drugs = data_loader.load_drugs()
    pubmed = data_loader.load_pubmed()

    cleaner_trials = DataCleaner(clinical_trials)
    cleaned_trials = cleaner_trials.clean()

    cleaner_drugs = DataCleaner(drugs)
    cleaned_drugs = cleaner_drugs.clean()

    cleaner_pubmed = DataCleaner(pubmed)
    cleaned_pubmed = cleaner_pubmed.clean()

    drug_mentions_clinical_trials = drug_mentions(cleaned_trials, cleaned_drugs, 'clinical_trials')
    drug_mentions_pubmed = drug_mentions(cleaned_pubmed, cleaned_drugs, 'pubmed')

    merged_data = merge_data(drug_mentions_clinical_trials, drug_mentions_pubmed)

    graph = build_data_graph(merged_data, cleaned_drugs)

    save_graph_to_json(graph)

if __name__ == "__main__":
    run_data_pipeline()