import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Find the count of all submatrices of the given matrix that contain 173 integers each.
    """
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrices.append(matrix[i:k + 1, j:l + 1])
    count = 0
    for submatrix in submatrices:
        if submatrix.size == 173:
            count += 1
    return count