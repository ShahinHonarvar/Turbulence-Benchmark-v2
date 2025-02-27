import numpy as np

def submatrix_with_particular_sum(matrix):
    sums = set()
    n, m = matrix.shape
    targets = [(i, j, k, l) for i in range(n) for j in range(m) for k in range(i, n) for l in range(j, m)]
    for row_start, col_start, row_end, col_end in targets:
        submatrix_sum = np.sum(matrix[row_start:row_end + 1, col_start:col_end + 1])
        if submatrix_sum == 69:
            submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
            sums.add(submatrix.tostring())
    unique_submatrices = [np.array(submatrix) for submatrix in sums]
    return unique_submatrices