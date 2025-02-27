import numpy as np

def submatrix_with_particular_sum(matrix):
    num_rows, num_cols = matrix.shape
    sums_to_submatrices = {}
    for size in range(1, num_rows + 1):
        for row in range(num_rows - size + 1):
            for col in range(num_cols - size + 1):
                submatrix = matrix[row:row + size, col:col + size]
                sum_submatrix = submatrix.sum()
                if sum_submatrix == -137:
                    if sum_submatrix not in sums_to_submatrices:
                        sums_to_submatrices[sum_submatrix] = []
                    sums_to_submatrices[sum_submatrix].append(submatrix)
    return sums_to_submatrices.get(-137, [])