from sklearn.feature_extraction.text import CountVectorizer

def extract_features(data):
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=1000, stop_words='english')
    data = vectorizer.fit_transform(data)
    return data

