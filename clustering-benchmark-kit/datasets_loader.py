import numpy as npfrom sklearn import datasetsfrom sklearn.preprocessing import StandardScalerfrom sklearn.datasets import make_moons, make_circles, make_blobsdef load_all_datasets():    dataset_dict = {}    # 🌕 Moons    X, y = make_moons(n_samples=500, noise=0.05, random_state=42)    dataset_dict["moons"] = (StandardScaler().fit_transform(X), y)    # ⭕ Circles    X, y = make_circles(n_samples=500, noise=0.05, factor=0.5, random_state=42)    dataset_dict["circles"] = (StandardScaler().fit_transform(X), y)    # 🎯 Blobs (well-separated)    X, y = make_blobs(n_samples=500, centers=3, random_state=42)    dataset_dict["blobs"] = (StandardScaler().fit_transform(X), y)    # 🧬 Iris    iris = datasets.load_iris()    dataset_dict["iris"] = (StandardScaler().fit_transform(iris.data), iris.target)    # 💻 Digits (subset of MNIST-style)    digits = datasets.load_digits()    X = StandardScaler().fit_transform(digits.data)    y = digits.target    dataset_dict["digits"] = (X, y)    # 🔢 Wine    wine = datasets.load_wine()    dataset_dict["wine"] = (StandardScaler().fit_transform(wine.data), wine.target)    # 🧮 Breast Cancer    bc = datasets.load_breast_cancer()    dataset_dict["breast_cancer"] = (StandardScaler().fit_transform(bc.data), bc.target)    return dataset_dict