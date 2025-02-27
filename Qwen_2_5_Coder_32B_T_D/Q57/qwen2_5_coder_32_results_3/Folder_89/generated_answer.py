import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sums(matrix, target):
        submatrices = []
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(i, rows):
                current_sum = np.zeros(cols)
                for k in range(cols):
                    current_sum[k] += matrix[j, k]
                    total = 0
                    for start in range(cols):
                        total += current_sum[start]
                        if total == target:
                            submatrices.append(matrix[i:j + 1, start:k + 1])
        return submatrices
    return submatrix_sums(matrix, 80)