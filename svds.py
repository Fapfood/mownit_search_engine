from time import time

import numpy as np
from scipy.sparse import csc_matrix, load_npz
from scipy.sparse.linalg import svds

matrix = load_npz('resources/org_matrix.npz')

length = min(matrix.shape) // 5

t_start = time()
U, s, V = svds(matrix, k=length)
t_end = time()
print(t_end - t_start)
np.save('resources/U_matrix', U)
np.save('resources/s_matrix', s)
np.save('resources/V_matrix', V)


# t_start = time()
# m = np.zeros(matrix.shape)
# for i in range(length):
    # print(U[:, [i]] * V[i])
    # print(np.outer(U[:, i], V[i]))
    # m += np.outer(U[:, i], V[i]).dot(s[i])
# t_end = time()
# print(t_end - t_start)

# np.save('resources/cln_matrix', m)
# np.save('resources/cln_2_matrix', csc_matrix(m.round(6)))
