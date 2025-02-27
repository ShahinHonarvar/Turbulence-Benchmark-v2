import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            if c + 1 < cols:
                submatrix = matrix[r, c:c + 2]
                if len(set(submatrix)) == 2:
                    count += 1
            if r + 1 < rows:
                submatrix = matrix[r:r + 2, c]
                if len(set(submatrix)) == 2:
                    count += 1
            if r + 1 < rows and c + 1 < cols:
                submatrix = matrix[r:r + 2, c:c + 2]
                if len(set(submatrix.flatten())) == 2:
                    count += 1
    return count