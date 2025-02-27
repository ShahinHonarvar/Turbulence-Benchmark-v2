import numpy as np

def submatrix_with_particular_sum(matrix):

    def generate_submatrices(mat, r, c):
        submatrices = []
        for start_row in range(r):
            for start_col in range(c):
                for end_row in range(start_row + 1, r + 1):
                    for end_col in range(start_col + 1, c + 1):
                        submatrices.append(mat[start_row:end_row, start_col:end_col])
        return submatrices
    r, c = matrix.shape
    all_submatrices = generate_submatrices(matrix, r, c)
    result = [submat.tolist() for submat in all_submatrices if np.sum(submat) == -394]
    return result