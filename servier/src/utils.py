import re

def clean_text(text):
    """Clean text by removing unwanted characters and normalizing."""
    if isinstance(text, str):
        text = bytes(text, 'latin1').decode('utf-8', 'replace')
        text = re.sub(r'[^\w\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text.lower()
    return text

def remove_special_character(text):
    """Remove special characters from the text."""
    if isinstance(text, str):
        return re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

def replace_punctuation(text):
    """Replace punctuation in the text with a space."""
    if isinstance(text, str):
        return re.sub(r'[!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]', ' ', text)
    return text

def clean_special_patterns(text):
    """Clean specific patterns from the text."""
    if isinstance(text, str):
        patterns = [
            (r'\\xc3\\x28', ''),
            (r'\xc3\x28', ''),
            (r'\\xc3\\xb1', 'ñ'),
            (r'\xc3\xb1', 'ñ'),
            (r'™', ''),
            (r'\\u00f4', 'ô'),
            (r'\\u00e8', 'è'),
            (r'\u00f4', 'ô'),         
            (r'\u00e8', 'è'),
        ]
        
        cleaned_text = text
        for pattern, replacement in patterns:
            cleaned_text = re.sub(pattern, replacement, cleaned_text)
        
        return cleaned_text
    return text

def clean_text_combined(text):
    """Combine cleaning methods to clean text."""
    text = clean_special_patterns(text)  # Clean specific patterns
    text = clean_text(text)  # Use the existing function
    text = remove_special_character(text)  # Remove special characters
    text = replace_punctuation(text)  # Replace punctuation
    return text