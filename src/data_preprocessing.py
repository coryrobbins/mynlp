import re

def clean_text(text: str) -> str:
    text = text.lower() # Convert to lowercase
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text) # Remove special characters
    text = re.sub(r'\n', ' ', text) # Replace newlines with whitespace
    text = re.sub(r'\s+', ' ', text) # Replace multiple whitespaces with single whitespace
    return text

