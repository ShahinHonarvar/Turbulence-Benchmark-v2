import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for i in range(row):
        for j in range(col):
            for k in range(i, row):
                for l in range(j, col):
                    sub_matrix = matrix[i:k + 1, j:l + 1]
                    num_integers = sub_matrix.size
                    if num_integers == 185:
                        count += 1
    return count