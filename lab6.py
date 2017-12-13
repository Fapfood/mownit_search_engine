import collections
from collections import defaultdict
from re import findall

from math import log
from nltk.corpus import stopwords
from nltk.stem.porter import *
from time import time
import numpy as np
from scipy import sparse
import lda

# import nltk
# nltk.download("stopwords")
STOPWORDS = stopwords.words('english')


class Document:
    def __init__(self, text, vector):
        self.text = text
        self.vector = vector


def build_documents(texts, scale_by_idf=False):
    stemmer = PorterStemmer()
    bags_of_words = [collections.Counter(
        [stemmer.stem(word) for word in map(lambda w: w.lower(), findall(r'\w+', txt)) if word not in STOPWORDS]
    ) for txt in texts]

    documents_count = len(texts)

    bags_of_words_with_default = []
    vocabulary_count = defaultdict(int)

    for bag_of_words in bags_of_words:
        bag_of_words_with_default = defaultdict(int)
        for k, v in bag_of_words.items():
            vocabulary_count[k] += 1
            bag_of_words_with_default[k] = v
        bags_of_words_with_default.append(bag_of_words_with_default)

    idf = dict()
    for k, v in vocabulary_count.items():
        idf[k] = log(documents_count / v)

    documents = []
    for i, bag in enumerate(bags_of_words_with_default):
        if scale_by_idf:
            for k in bag.keys():
                bag[k] *= idf[k]
        documents.append(Document(texts[i], bag))

    return documents, vocabulary_count


def convert_documents_into_sparse_matrix(documents, vocab):
    matrix = []
    for document in documents:
        vector = document.vector
        row = [vector[v] for v in vocab]
        matrix.append(row)
    np_matrix = np.matrix(matrix)
    return sparse.dok_matrix(np_matrix)


with open('resources/training_set_tweets_clean.txt', 'r', encoding='utf8') as read_file:
    texts = read_file.read().splitlines()[:10000]

t_start = time()
documents, vocabulary_count = build_documents(texts)
vocab = list(vocabulary_count.keys())
t_end = time()
print(t_end - t_start)
matrix = convert_documents_into_sparse_matrix(documents, vocab)
print(matrix)
model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
model.fit(matrix)
topic_word = model.topic_word_
print(topic_word)
topic_word = model.topic_word_  # model.components_ also works
n_top_words = 8
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words + 1):-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))
