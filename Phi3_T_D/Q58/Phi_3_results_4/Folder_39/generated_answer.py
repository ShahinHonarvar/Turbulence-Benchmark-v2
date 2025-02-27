import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for w in range(i + 1, rows + 1):
                if w - i == 59:
                    break
                for h in range(j + 1, cols + 1):
                    if h - j == 59:
                        break
                    if w - i == h - j == 59:
                        count += 1
    return count