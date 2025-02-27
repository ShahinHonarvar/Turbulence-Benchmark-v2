import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Find the count of all submatrices in a given matrix that contain 5 numbers.
    """
    count = 0
    for i in range(len(matrix) - 4):
        for j in range(len(matrix[0]) - 4):
            submatrix = matrix[i:i + 5, j:j + 5]
            if submatrix.size == 5:
                count += 1
    return count