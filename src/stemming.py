from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def stem_tokens(tokens: list) -> list:
    return [stemmer.stem(token) for token in tokens]

