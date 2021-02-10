import numpy as np
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import re
import pickle


def cleanString(st):
    new_string = re.sub('[^A-z0-9 -]', '', st).lower()
    f_string = ""
    for word in new_string.split(' '):
        if not word.isdigit():
            if (word.endswith('g') or word.endswith('ml')) and word[0].isdigit():
                pass
            elif word == 'g' or word == 'ml':
                pass
            else:
                f_string += (word + ' ')

    f_string = f_string.replace('-', '')
    f_string = f_string.strip()
    return f_string


def train_model():

    dt = pd.read_csv('Raw_Data.csv')

    data = list(dt['Discription'])

    document = list(map(cleanString, data))

    # text vectrization
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(document)

    # kmeans
    true_k = 3
    model = KMeans(n_clusters=true_k, init='k-means++',
                   max_iter=1000, n_init=10, random_state=1)
    model.fit(X)

    # Formation of centroid
    centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()


# print(centroids)
# print(terms)
'''
for i in range(true_k):
    print("Cluster %d:" % i,)
    for ind in centroids[i, :10]:
        print("%s" % terms[ind])

pickle.dump(model, open("Model", 'wb'))
'''
# train_model()
