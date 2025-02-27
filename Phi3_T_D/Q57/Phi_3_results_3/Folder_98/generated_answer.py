import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []

    def gen_submatrices(submatrix):
        if submatrix is not None:
            for i in range(len(submatrix)):
                if submatrix[i].size > 1:
                    results.append(submatrix[i])
                if len(submatrix[i]) > 1:
                    gen_submatrices(submatrix[i:])
                submatrix[i:i + 1] = []

    def search(matrix):
        if matrix.size > 1:
            submatrices_top = [matrix[0:col] for col in range(1, matrix.shape[1] + 1)]
            search(np.array(submatrices_top))
            submatrices_left = [matrix[row:row + 1, :] for row in range(1, matrix.shape[0] + 1)]
            search(np.array(submatrices_left))
            submatrices_top_left = [matrix[0:row, 0:col] for row in range(1, matrix.shape[0] + 1) for col in range(1, matrix.shape[1] + 1)]
            search(np.array(submatrices_top_left))
            gen_submatrices(submatrices_top_left)
    search(matrix)
    return [submatrix for submatrix in results if np.sum(submatrix) == 0]