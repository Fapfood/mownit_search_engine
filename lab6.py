import collections
from collections import defaultdict
from re import findall

from math import log
from nltk.corpus import stopwords
from nltk.stem.porter import *
from time import time

# import nltk
# nltk.download("stopwords")
STOPWORDS = stopwords.words('english')


class Document:
    def __init__(self, text, vector):
        self.text = text
        self.vector = vector


def build_documents(texts):
    stemmer = PorterStemmer()
    bags_of_words = [collections.Counter(
        [stemmer.stem(word) for word in map(lambda w: w.lower(), findall(r'\w+', txt)) if word not in STOPWORDS]
    ) for txt in texts]

    document_count = len(bags_of_words)

    full_bags_of_words = []
    c = defaultdict(int)
    for d in bags_of_words:
        full_bag_of_words = defaultdict(int)
        for k, v in d.items():
            c[k] += 1
            full_bag_of_words[k] = v
        full_bags_of_words.append(full_bag_of_words)

    idf = dict()
    for k, v in c.items():
        idf[k] = log(document_count / v)

    documents = []
    for i, bag in enumerate(full_bags_of_words):
        for k in bag.keys():
            bag[k] *= idf[k]
        documents.append(Document(texts[i], bag))

    return documents


with open('resources/training_set_tweets_clean.txt', 'r', encoding='utf8') as read_file:
    texts = read_file.read().splitlines()

t_start = time()
full_bags_of_words = build_documents(texts)
t_end = time()
print(t_end - t_start)
# for d in full_bags_of_words:
#     print(d.text, d.vector)
