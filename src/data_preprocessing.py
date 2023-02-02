import re
import string

def space_after_punc(text):
    spaced_text = ''
    for char in text:
        if char in string.punctuation:
            spaced_text += char + ' '
        else:
            spaced_text += char
    return spaced_text

def remove_punctuation(text):
    new_text = ''
    for char in text:
        if char not in string.punctuation:
            new_text = new_text + char
    return new_text

def clean_text(text: str) -> str:
    text = space_after_punc(text)
    text = text.lower() # Convert to lowercase
    text = re.sub(r'\r+|\n+||\t', '', regex=True) # removes line breaks, indentions etc. 
    text = re.sub(r'XYZ', ' ', text) #removes XYZ from anonymization
    text = re.sub(r'<[^<>]*>', '', regex=True) #removal of HTML
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text) # Remove special characters
    text = re.sub(r'\n', ' ', text) # Replace newlines with whitespace
    text = re.sub(r'\s+', ' ', text) # Replace multiple whitespaces with single whitespace
    return text
