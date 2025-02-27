import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input should be a numpy array')
    submatrices = []
    number_of_rows, number_of_columns = matrix.shape
    for top in range(number_of_rows):
        for left in range(number_of_columns):
            for bottom in range(top + 1, number_of_rows + 1):
                for right in range(left + 1, number_of_columns + 1):
                    submatrix = matrix[top:bottom, left:right]
                    if submatrix.sum() == 34:
                        submatrices.append(submatrix)
    return submatrices