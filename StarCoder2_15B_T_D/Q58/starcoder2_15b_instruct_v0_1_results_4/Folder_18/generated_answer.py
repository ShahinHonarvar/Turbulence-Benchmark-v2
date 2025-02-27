import numpy as np

def submatrix_with_n_numbers(matrix, n=104):
    """
    Returns the count of all submatrices in `matrix` that contain `n` numbers.
    """
    nrows, ncols = matrix.shape
    count = 0
    for i in range(nrows - 2):
        for j in range(ncols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.count_nonzero(submatrix) == n:
                count += 1
    return count