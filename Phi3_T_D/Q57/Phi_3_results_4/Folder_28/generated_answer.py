import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    results = []

    def explore(r1, c1, r2, c2):
        current_sum = np.sum(matrix[r1:r2 + 1, c1:c2 + 1])
        if current_sum == 15:
            results.append(matrix[r1:r2 + 1, c1:c2 + 1].copy())
        for i in range(r1, r2 + 1):
            explore(i, c1, i, c2)
        for i in range(c1, c2 + 1):
            explore(r1, i, r2, i)
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                matrix[i, j] += current_sum
        for i in range(r1, r2 + 1):
            matrix[i, c1] -= current_sum
        for i in range(c1, c2 + 1):
            matrix[r2, i] -= current_sum
        matrix[r1, c1] -= current_sum
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    matrix_copy = matrix.copy()
                    explore(r1, c1, r2, c2)
                    matrix_copy = matrix.copy()
                    if matrix_copy[r1, c1] == matrix_copy[r2, c2]:
                        results.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return results