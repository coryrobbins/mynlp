import nltk
nltk.download('punkt')

def tokenize(text: str) -> list:
    return nltk.word_tokenize(text)

