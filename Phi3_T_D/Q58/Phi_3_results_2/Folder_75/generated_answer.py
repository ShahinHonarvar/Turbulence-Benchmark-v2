import numpy as np

def submatrix_with_n_numbers(matrix, n=80):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            current_count = 0
            for m in range(i, rows):
                for n in range(j, cols):
                    current_count += 1
                    if current_count >= n:
                        count += 1
    return count