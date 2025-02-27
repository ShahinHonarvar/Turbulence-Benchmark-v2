import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def check_sum(sub_matrix):
        return np.sum(sub_matrix) == -83

    def include_element(i, j, sum_submatrix):
        if check_sum(sum_submatrix):
            result.append(sum_submatrix)
    for i in range(rows):
        for j in range(cols):
            for m in range(i, rows):
                for n in range(j, cols):
                    sum_submatrix = np.zeros((m - i + 1, n - j + 1), dtype=int)
                    sum_submatrix += matrix[i:m + 1, j:n + 1]
                    include_element(i, j, sum_submatrix)
    return result