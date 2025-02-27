import numpy as np

def submatrix_with_n_numbers(matrix, n=85):
    matrix = np.array(matrix)
    count = 0
    num_rows, num_cols = matrix.shape
    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(i, num_rows):
                for l in range(j, num_cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == n:
                        count += 1
    return count