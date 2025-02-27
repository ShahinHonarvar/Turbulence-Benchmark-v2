import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Returns the count of all submatrices of the given matrix that contain 5 integers each.
    """
    submatrix_count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for i in range(row, len(matrix)):
                for j in range(col, len(matrix[0])):
                    submatrix = matrix[row:i + 1, col:j + 1]
                    if submatrix.size == 5:
                        submatrix_count += 1
    return submatrix_count