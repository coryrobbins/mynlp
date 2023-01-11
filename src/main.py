import data_preprocessing as dp
import tokenization as tk
import stopword_removal as sw
import stemming as st
import lemmatization as lm
import topic_modeling as tm
import feature_extraction as ft
import model_training as mt
import model_evaluation as me
import model_inference as mi

def main():
    raw_data = dp.load_data("data/raw/emails.csv")
    preprocessed_data = dp.clean_text(raw_data)
    tokenized_data = tk.tokenize(preprocessed_data)
    data_without_stopwords = sw.remove_stopwords(tokenized_data)
    stemmed_data = st.stem_tokens(data_without_stopwords)
    lemmatized_data = lm.lemmatize_tokens(stemmed_data)
    topic_model = tm.perform_topic_modelling(lemmatized_data)
    features = ft.extract_features(lemmatized_data)
    model = mt.train_model(features)
    evaluation = me.evaluate_model(model, features)
    mi.predict(model, features)

if __name__ == "__main__":
    main()

