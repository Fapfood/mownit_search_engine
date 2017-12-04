import collections
from re import findall, sub, subn

from nltk.corpus import stopwords
from nltk.stem.porter import *

# import nltk
# nltk.download("stopwords")
# with open('training_tweets.txt', 'r', encoding='utf8') as file:
#     texts = []
#     s = None
#     for line in file.read().splitlines():
#         line = sub(r'\d+\s+\d+\s+', '', line)
#         line, n = subn(r'\s+\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}', '', line)
#         if s is None:
#             s = line
#         else:
#             s += ' ' + line
#         if n > 0:
#             texts.append(s)
#             s = None

with open('c:/kurwa.txt', 'a+') as file:
    file.write('g\n')


# stemmer = PorterStemmer()
# bags_of_words = [collections.Counter(
#     [stemmer.stem(word) for word in findall(r'\w+', txt) if word not in stopwords.words('english')]) for txt in
#     texts]
# sum_bags = sum(bags_of_words, collections.Counter())
# print(sum_bags)
