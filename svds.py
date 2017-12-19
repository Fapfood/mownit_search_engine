from time import time

import numpy as np
from scipy.sparse import csc_matrix, save_npz, load_npz
from scipy.sparse.linalg import svds

matrix = load_npz('resources/org_matrix.npz')
length = min(matrix.shape) // 5
shape = matrix.shape

# t_start = time()
# U, s, V = svds(matrix, k=length)
# t_end = time()
# print(t_end - t_start)
# np.save('resources/U_matrix', U)
# np.save('resources/s_matrix', s)
# np.save('resources/V_matrix', V)

U = np.load('resources/U_matrix.npy')
s = np.load('resources/s_matrix.npy')
V = np.load('resources/V_matrix.npy')

t_start = time()

# m = np.zeros(shape)
for i in range(length):
    t_start = time()
    for j in range(shape[0]):
        V[i].dot(U[j, i]).dot(s[i])
    t_end = time()
    print(t_end - t_start)

# np.save('resources/cln_matrix', m)
# save_npz('resources/cln_matrix', csc_matrix(m.round(6)))
