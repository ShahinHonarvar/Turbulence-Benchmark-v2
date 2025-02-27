import numpy as np

def submatrix_with_n_numbers(matrix, n=46):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            current_sum = 0
            for k in range(i, rows):
                current_sum += matrix[k, j:min(cols, j + n)].sum()
                if current_sum == n:
                    count += 1
                elif current_sum > n:
                    break
    return count