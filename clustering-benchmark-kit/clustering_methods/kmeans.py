from sklearn.cluster import KMeansimport timedef kmeans_cluster(X, n_clusters=None):    start = time.time()    if not n_clusters:        # Estimate number of clusters using simple heuristic        n_clusters = len(set(KMeans(n_init=10).fit_predict(X)))    model = KMeans(n_clusters=n_clusters, n_init=10, random_state=42)    y_pred = model.fit_predict(X)    end = time.time()    return y_pred, start, end