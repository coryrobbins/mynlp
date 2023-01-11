import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def lemmatize_tokens(tokens: list) -> list:
    return [lemmatizer.lemmatize(token) for token in tokens]

