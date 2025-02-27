import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, rows, cols):
        submats = []
        for r in range(rows):
            for c in range(cols):
                for r_end in range(r + 1, rows + 1):
                    for c_end in range(c + 1, cols + 1):
                        submats.append(matrix[r:r_end, c:c_end])
        return submats
    rows, cols = matrix.shape
    all_submatrices = submatrices(matrix, rows, cols)
    result = [submat for submat in all_submatrices if np.sum(submat) == 15]
    return result