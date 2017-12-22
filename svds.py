from time import time

import numpy as np
from scipy.sparse import csc_matrix, save_npz, load_npz
from scipy.sparse.linalg import svds

"""SCALE BY IDF AND NORMALIZE"""
# matrix = load_npz('resources/org_matrix.npz')
# length = min(matrix.shape) // 5
# shape = matrix.shape

# t_start = time()
# U, s, V = svds(matrix, k=length)
# t_end = time()
# print(t_end - t_start)
# np.save('resources/U_matrix', U)
# np.save('resources/s_matrix', s)
# np.save('resources/V_matrix', V)

# U = np.load('resources/U_matrix.npy')
# s = np.load('resources/s_matrix.npy')
# V = np.load('resources/V_matrix.npy')
# t_start = time()
# m = np.zeros(shape)
# for i in range(length):
#     print(i)
#     for j in range(shape[0]):
#         m[j] += V[i].dot(s[i] * U[j, i])
# t_end = time()
# print(t_end - t_start)
# np.save('resources/cln_matrix', m)

# matrix = np.load('resources/cln_matrix.npy').round(6)
# csc_matrix = csc_matrix(matrix)
# save_npz('resources/cln_sparse_matrix', csc_matrix)

"""NOT SCALE BY IDF BUT NORMALIZE"""
matrix = load_npz('resources/org_nonscale_but_normalise_matrix.npz')
length = min(matrix.shape) // 5
shape = matrix.shape

# t_start = time()
# U, s, V = svds(matrix, k=length)
# t_end = time()
# print(t_end - t_start)
# np.save('resources/U_nonscale_but_normalise_matrix', U)
# np.save('resources/s_nonscale_but_normalise_matrix', s)
# np.save('resources/V_nonscale_but_normalise_matrix', V)

U = np.load('resources/U_nonscale_but_normalise_matrix.npy')
s = np.load('resources/s_nonscale_but_normalise_matrix.npy')
V = np.load('resources/V_nonscale_but_normalise_matrix.npy')
t_start = time()
m = np.zeros(shape)
for i in range(length):
    print(i)
    for j in range(shape[0]):
        m[j] += V[i].dot(s[i] * U[j, i])
t_end = time()
print(t_end - t_start)
np.save('resources/cln_nonscale_but_normalise_matrix', m)

# matrix = np.load('resources/cln_nonscale_but_normalise_matrix.npy').round(6)
# csc_matrix = csc_matrix(matrix)
# save_npz('resources/cln_sparse_nonscale_but_normalise_matrix', csc_matrix)
