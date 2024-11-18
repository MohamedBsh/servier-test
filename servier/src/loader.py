import pandas as pd
import json
from config import *

class DataLoader:
    def __init__(self, config: object):
        """
        Initializes the DataLoader with a configuration object.

        Args:
            config (object): The configuration object containing file paths.
        """
        self.config = config

    def load_clinical_trials(self) -> pd.DataFrame:
        """
        Loads clinical trials data from a CSV file.

        Returns:
            pd.DataFrame: A DataFrame containing clinical trials data.
        """
        return pd.read_csv(self.config.CLINICAL_TRIALS_FILE)

    def load_drugs(self) -> pd.DataFrame:
        """
        Loads drug data from a CSV file.

        Returns:
            pd.DataFrame: A DataFrame containing drug data.
        """
        return pd.read_csv(self.config.DRUGS_FILE)

    def load_pubmed(self) -> pd.DataFrame:
        """
        Loads PubMed data from a CSV file and a JSON file, then concatenates them.

        Returns:
            pd.DataFrame: A DataFrame containing combined PubMed data.
        """
        pubmed_csv = pd.read_csv(self.config.PUBMED_CSV_FILE)
        pubmed_json = self.load_pubmed_json()
        return pd.concat([pubmed_csv, pubmed_json], ignore_index=True)

    def load_pubmed_json(self) -> pd.DataFrame:
        """
        Loads PubMed data from a JSON file and normalizes it into a DataFrame.

        Returns:
            pd.DataFrame: A DataFrame containing PubMed data from the JSON file.
        """
        with open(self.config.PUBMED_JSON_FILE, 'r') as f:
            return pd.json_normalize(json.load(f))