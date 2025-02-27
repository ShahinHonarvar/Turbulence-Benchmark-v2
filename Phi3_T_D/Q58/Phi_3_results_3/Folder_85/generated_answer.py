import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            for k in range(i, size):
                for l in range(j, size):
                    if k - i + 1 == l - j + 1 == 13:
                        test_submatrix = matrix[i:k + 1, j:l + 1]
                        if np.count_nonzero(test_submatrix) == 13:
                            count += 1
    return count