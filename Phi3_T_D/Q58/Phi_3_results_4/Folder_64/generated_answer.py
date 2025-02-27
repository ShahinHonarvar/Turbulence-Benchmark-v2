import numpy as np

def submatrix_with_n_numbers(mat):
    rows, cols = mat.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for s in range(1, rows - i + 1):
                if rows - i >= 7:
                    for t in range(1, cols - j + 1):
                        if cols - j >= 7:
                            count += 1
                        else:
                            break
                else:
                    break
    return count