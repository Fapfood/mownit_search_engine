from time import time

import lda
import numpy as np
from scipy.sparse import load_npz


def latent_dirichlet_allocation(matrix, n_topics=100, n_iter=10_000, measure_time=True,
                                save=True, save_path='resources/topic_matrix'):
    """NOT WORK WITH FLOAT VALUES"""
    t_start = time()

    model = lda.LDA(n_topics=n_topics, n_iter=n_iter, random_state=1)
    model.fit(matrix.T)
    topic_word = model.topic_word_  # model.components_ also works

    t_end = time()

    if measure_time:
        print('lta time:', t_end - t_start)

    if save:
        np.save(save_path, topic_word)

    return topic_word


def get_topics(topic_matrix, vocab, n_top_words=20, measure_time=True, save_path='resources/topic_list.txt'):
    t_start = time()

    with open(save_path, 'w', encoding='utf8') as file:
        for i, topic_dist in enumerate(topic_matrix):
            topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words + 1):-1]
            file.write('Topic {}: {}\n'.format(i, ' '.join(topic_words)))

    t_end = time()

    if measure_time:
        print('get topics time:', t_end - t_start)


matrix = load_npz('resources/org_nonscale_matrix.npz')
topic_matrix = latent_dirichlet_allocation(matrix, n_topics=150, n_iter=30_000)
with open('resources/vocabulary.txt', 'r', encoding='utf8') as vocabulary:
    vocab = vocabulary.readline().split(' ')
get_topics(topic_matrix, vocab)
