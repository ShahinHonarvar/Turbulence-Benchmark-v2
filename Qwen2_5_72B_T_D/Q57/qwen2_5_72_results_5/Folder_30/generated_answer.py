import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, rows, cols):
        submatrices_list = []
        for i in range(rows):
            for j in range(cols):
                for p in range(i + 1, rows + 1):
                    for q in range(j + 1, cols + 1):
                        submatrices_list.append(matrix[i:p, j:q])
        return submatrices_list
    rows, cols = matrix.shape
    all_submatrices = submatrices(matrix, rows, cols)
    result = [submat for submat in all_submatrices if np.sum(submat) == 21]
    return result