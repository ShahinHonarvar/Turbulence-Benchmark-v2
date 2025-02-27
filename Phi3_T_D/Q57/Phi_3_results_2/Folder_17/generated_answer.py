import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix')
    rows, cols = matrix.shape
    target_sum = 398
    results = []

    def get_all_submatrices(r1, c1, rows, cols):
        for i in range(r1, rows):
            for j in range(c1, cols):
                for k in range(i, rows):
                    for l in range(j, cols):
                        submatrix = matrix[i:k + 1, j:l + 1]
                        if np.sum(submatrix) == target_sum:
                            results.append(submatrix)
    for row_start in range(rows):
        for col_start in range(cols):
            get_all_submatrices(row_start, col_start, rows, cols)
    return results