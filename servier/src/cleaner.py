import pandas as pd
from utils import clean_text_combined

class DataCleaner:
    def __init__(self, df: pd.DataFrame) -> None:
        """
        Initializes the DataCleaner with a DataFrame.

        Args:
            df (pd.DataFrame): The DataFrame to be cleaned.
        """
        self.df = df

    def clean(self) -> pd.DataFrame:
        """
        Cleans the DataFrame by applying text cleaning and date formatting.

        Returns:
            pd.DataFrame: The cleaned DataFrame.
        """
        if 'scientific_title' in self.df.columns:
            self.df['scientific_title'] = self.df['scientific_title'].apply(clean_text_combined)
            self.df['scientific_title'] = self.df['scientific_title'].replace(r'^\s*$', pd.NA, regex=True)

        if 'journal' in self.df.columns:
            self.df['journal'] = self.df['journal'].apply(clean_text_combined)

        if 'date' in self.df.columns:
            self.df['date'] = self.df['date'].apply(self.clean_date)

        columns_to_check = ['scientific_title', 'journal']
        if all(col in self.df.columns for col in columns_to_check):
            self.df.dropna(subset=columns_to_check, inplace=True)

        return self.df
    
    def clean_date(self, date_str: str) -> pd.Timestamp:
        """
        Cleans and formats a date string into a pandas Timestamp.

        Args:
            date_str (str): The date string to be cleaned.

        Returns:
            pd.Timestamp: The cleaned date as a Timestamp, or pd.NaT if the date is invalid.
        """
        if pd.isna(date_str):
            return pd.NaT
                
        try:
            if isinstance(date_str, str):
                if '-' in date_str:
                    return pd.to_datetime(date_str)
                elif '/' in date_str:
                    return pd.to_datetime(date_str, format='%d/%m/%Y')
                else:
                    return pd.to_datetime(date_str, format='%d %B %Y')
            return pd.to_datetime(date_str)
        except Exception as e:
            print(f"Error: {e}")
            return pd.NaT