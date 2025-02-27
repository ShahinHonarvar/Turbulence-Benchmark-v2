import numpy as np

def submatrix_with_particular_sum(matrix):

    def generate_submatrices(mat, rows, cols):
        submatrices = []
        for top in range(rows):
            for left in range(cols):
                for bottom in range(top + 1, rows + 1):
                    for right in range(left + 1, cols + 1):
                        submatrices.append(mat[top:bottom, left:right])
        return submatrices
    target_sum = -43
    rows, cols = matrix.shape
    all_submatrices = generate_submatrices(matrix, rows, cols)
    result = [submat.tolist() for submat in all_submatrices if np.sum(submat) == target_sum]
    return result