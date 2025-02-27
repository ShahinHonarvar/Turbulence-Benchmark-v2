import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for top in range(m):
        for bottom in range(top, m):
            for left in range(n):
                for right in range(left, n):
                    if np.sum(matrix[top:bottom + 1, left:right + 1].size) == 87:
                        count += 1
    return count