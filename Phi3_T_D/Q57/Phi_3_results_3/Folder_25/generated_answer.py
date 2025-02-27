import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    sums = np.zeros((rows + 1, cols + 1), dtype=int)
    sums[1:, 1:] = np.cumsum(np.cumsum(matrix, axis=0), axis=1)
    for start1 in range(1, rows + 1):
        for start2 in range(1, cols + 1):
            for end1 in range(start1, rows + 1):
                for end2 in range(start2, cols + 1):
                    submatrix_sum = sums[end1, end2] - sums[start1 - 1, end2] - sums[end1, start2 - 1] + sums[start1 - 1, start2 - 1]
                    if submatrix_sum == -20:
                        result.append(matrix[start1 - 1:end1, start2 - 1:end2])
    return result