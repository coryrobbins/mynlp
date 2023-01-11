from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def remove_stopwords(tokens: list) -> list:
    return [token for token in tokens if token not in stop_words]

