import collections
from collections import defaultdict
from math import log
from re import findall
from time import time

import numpy as np
from nltk.corpus import stopwords
from nltk.stem.porter import *
from scipy.sparse import hstack, csc_matrix, save_npz

# import nltk
# nltk.download("stopwords")
STOPWORDS = stopwords.words('english')


class Document:
    def __init__(self, text, vector):
        self.text = text
        self.vector = vector


def read_data(number_of_rows, measure_time=True):
    t_start = time()

    with open('resources/training_set_tweets_clean_3.txt', 'r', encoding='utf8') as read_file:
        texts = read_file.read().splitlines()[:number_of_rows]

    t_end = time()

    if measure_time:
        print('read file time:', t_end - t_start)

    return texts


def build_documents(texts, scale_by_idf=True, normalize=True, measure_time=True):
    t_start = time()

    stemmer = PorterStemmer()
    bags_of_words = [collections.Counter(
        [stemmer.stem(word) for word in map(lambda w: w.lower(), findall(r'\w+', txt)) if word not in STOPWORDS]
    ) for txt in texts]

    documents_count = len(texts)

    vocabulary_count = defaultdict(int)
    for bag_of_words in bags_of_words:
        for k, v in bag_of_words.items():
            vocabulary_count[k] += 1
    vocabulary_count = dict(vocabulary_count)

    if scale_by_idf:
        idf = dict()
        for k, v in vocabulary_count.items():
            idf[k] = log(documents_count / v)

    documents = []
    for i, bag in enumerate(bags_of_words):
        if scale_by_idf:
            for k in bag.keys():
                bag[k] *= idf[k]
        if normalize:
            s = sum(bag.values())
            for k in bag.keys():
                bag[k] /= s
        documents.append(Document(texts[i], bag))

    t_end = time()

    if measure_time:
        print('build documents time:', t_end - t_start)

    return documents, vocabulary_count


def build_vocab(vocabulary_count, remove_most_common_fraction=0.1, measure_time=True,
                save=True, save_path='resources/vocabulary.txt'):
    t_start = time()

    sorted_dict = sorted(vocabulary_count.items(), key=lambda x: x[1], reverse=True)
    sorted_list = [k for k, v in sorted_dict]
    index = round(len(sorted_list) * remove_most_common_fraction)
    sorted_list = sorted_list[index:]

    t_end = time()

    if measure_time:
        print('build vocab time:', t_end - t_start)

    if save:
        with open(save_path, 'w', encoding='utf8') as vocabulary:
            vocabulary.write(' '.join(sorted_list))

    return sorted_list


def convert_documents_into_sparse_matrix(documents, vocab, dtype=np.float64, measure_time=True,
                                         save=True, save_path='resources/org_matrix'):
    t_start = time()

    matrix = csc_matrix((len(vocab), 0), dtype=dtype)
    for i, document in enumerate(documents):
        vector = document.vector
        column = csc_matrix([vector.get(v, 0) for v in vocab], dtype=dtype).T
        matrix = hstack([matrix, column])

    t_end = time()

    if measure_time:
        print('build sparse matrix time:', t_end - t_start)

    if save:
        save_npz(save_path, matrix)

    return matrix


"""SCALE BY IDF AND NORMALIZE"""
texts = read_data(30_000)
documents, vocabulary_count = build_documents(texts)
vocab = build_vocab(vocabulary_count)
matrix = convert_documents_into_sparse_matrix(documents, vocab)

"""NOT SCALE BY IDF BUT NORMALIZE"""
# texts = read_data(30_000)
# documents, vocabulary_count = build_documents(texts, scale_by_idf=False, normalize=True)
# vocab = build_vocab(vocabulary_count, save=False)
# matrix = convert_documents_into_sparse_matrix(documents, vocab, save_path='resources/org_nonscale_but_normalise_matrix')

"""NOT SCALE BUT IDF AND NOT NORMALIZE - TO USE IN LDA"""
# texts = read_data(30_000)
# documents, vocabulary_count = build_documents(texts, scale_by_idf=False, normalize=False)
# vocab = build_vocab(vocabulary_count, save=False)
# matrix = convert_documents_into_sparse_matrix(documents, vocab, dtype=np.int8, save_path='resources/org_nonscale_matrix')
