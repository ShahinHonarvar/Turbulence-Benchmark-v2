import numpy as np

def submatrix_with_n_numbers(matrix):
    result = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            count = 0
            for m in range(i, rows):
                for n in range(j, cols):
                    count += 1
                    if count == 38:
                        result += 1
                        break
                if count == 38:
                    break
    return result