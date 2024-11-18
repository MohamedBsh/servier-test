import pandas as pd
from typing import List, Dict, Any

def merge_data(clinical_mentions: List[Dict[str, Any]], pubmed_mentions: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Merges clinical mentions and PubMed mentions into a single DataFrame.

    Args:
        clinical_mentions (List[Dict[str, Any]]): A list of dictionaries containing clinical mentions data.
        pubmed_mentions (List[Dict[str, Any]]): A list of dictionaries containing PubMed mentions data.

    Returns:
        pd.DataFrame: A DataFrame containing the merged data from clinical and PubMed mentions.
    """
    merged = clinical_mentions + pubmed_mentions
    return pd.DataFrame(merged)