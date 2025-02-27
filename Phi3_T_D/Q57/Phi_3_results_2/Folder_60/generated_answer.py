import numpy as np

def get_submatrices(matrix, sum_target):
    shapes = [(i, j) for i in range(1, matrix.shape[0] + 1) for j in range(1, matrix.shape[1] + 1)]
    results = []
    for shape in shapes:
        for i in range(matrix.shape[0] - shape[0] + 1):
            for j in range(matrix.shape[1] - shape[1] + 1):
                submatrix = matrix[i:i + shape[0], j:j + shape[1]]
                if np.sum(submatrix) == sum_target:
                    results.append(submatrix)
    return results

def submatrix_with_particular_sum(matrix):
    return get_submatrices(matrix, 94)