import numpy as np

def submatrix_with_particular_sum(matrix):

    def check(m, i1, j1, i2, j2):
        return np.sum(m[i1:i2, j1:j2]) == -36

    def generate_submatrices(n, start, end):
        for i1 in range(start, end):
            for j1 in range(i1, end):
                for i2 in range(i1, end):
                    for j2 in range(j1, i2 + 1):
                        yield (i1, i2, j1, j2)
    result = []
    n = matrix.shape[0]
    for top_left in generate_submatrices(n, 0, n):
        i1, i2, j1, j2 = top_left
        if check(matrix, i1, j1, i2, j2):
            result.append(matrix[i1:i2 + 1, j1:j2 + 1].tolist())
    return result