import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def search(r1, c1, r2, c2, target):
        if r1 < r2 or c1 < c2:
            return
        current_sum = np.sum(matrix[r1:r2 + 1, c1:c2 + 1])
        if current_sum == target:
            result.append(matrix[r1:r2 + 1, c1:c2 + 1].tolist())
        search(r1, c1 + 1, r2, c2, target)
        search(r1, c1, r2, c2 + 1, target)
        search(r1 + 1, c1, r2, c2, target)
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    search(r1, c1, r2, c2, 901)
    return result