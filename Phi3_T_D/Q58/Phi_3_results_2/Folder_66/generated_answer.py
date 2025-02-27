import numpy as np

def submatrix_with_n_numbers(matrix, n=42):
    m = len(matrix)
    n = len(matrix[0])
    count = 0
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    sub_matrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(sub_matrix) == n * (n if k - i + 1 == n else 1):
                        count += 1
    return count