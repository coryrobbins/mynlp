from sklearn.decomposition import LatentDirichletAllocation

def perform_topic_modelling(data, n_components=10, n_features=1000):
    lda = LatentDirichletAllocation(n_components=n_components, max_iter=5, learning_method='online', learning_offset=50.,random_state=0)
    lda.fit(data)
    return lda

