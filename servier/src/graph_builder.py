import os
import json
import pandas as pd

OUTPUT_FILE = 'servier/data/drug_mentions_graph.json'

def build_data_graph(merged_data: pd.DataFrame, drugs: pd.DataFrame) -> dict:
    """
    Builds a data graph from merged data and drug information.

    Args:
        merged_data (pd.DataFrame): The DataFrame containing merged data.
        drugs (pd.DataFrame): The DataFrame containing drug information.

    Returns:
        dict: A dictionary representing the drug mentions graph.
    """
    graph = {"drugs": {}}

    for _, drug_row in drugs.iterrows():
        drug_name = drug_row['drug']
        drug_code = drug_row['atccode']
        graph["drugs"][drug_code] = {
            "pubmed_mentions": [],
            "clinical_trials": []
        }

        for _, mention in merged_data.iterrows():
            mention_dict = mention.to_dict()
            
            if isinstance(mention_dict['date'], pd.Timestamp):
                mention_dict['date'] = mention_dict['date'].strftime('%Y-%m-%d')
            else:
                mention_dict['date'] = ''

            if mention_dict['drug'] == drug_name:
                mention_id = str(mention_dict['id'])
                if 'NCT' in mention_id:  # check if the id is a clinical trial id
                    graph["drugs"][drug_code]["clinical_trials"].append(mention_dict)
                else:
                    graph["drugs"][drug_code]["pubmed_mentions"].append(mention_dict)

    return graph

def save_graph_to_json(graph: dict, output_file: str = OUTPUT_FILE) -> None:
    """
    Saves the graph to a JSON file.

    Args:
        graph (dict): The graph data to save.
        output_file (str): The path to the output JSON file.
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        json.dump(graph, f, indent=4)