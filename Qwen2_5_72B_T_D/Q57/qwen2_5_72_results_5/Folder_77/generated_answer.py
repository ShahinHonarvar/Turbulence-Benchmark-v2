import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(i, j, m, n):
        submatrices = []
        for x in range(i, m):
            for y in range(j, n):
                submatrix = matrix[i:x + 1, j:y + 1]
                if np.sum(submatrix) == -336:
                    submatrices.append(submatrix)
        return submatrices
    m, n = matrix.shape
    all_submatrices = []
    for i in range(m):
        for j in range(n):
            all_submatrices.extend(find_submatrices(i, j, m, n))
    return all_submatrices