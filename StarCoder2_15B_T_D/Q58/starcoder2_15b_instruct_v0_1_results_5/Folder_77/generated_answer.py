import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Finds the count of all submatrices of the given matrix that contain 179 integers each.
    """
    count = 0
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[0]) - 2):
            counter = 0
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    counter += matrix[k][l]
            if counter == 179:
                count += 1
    return count