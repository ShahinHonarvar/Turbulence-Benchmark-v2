import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(matrix):
        for x in range(0, matrix.shape[0]):
            for y in range(0, matrix.shape[1]):
                for width in range(1, matrix.shape[0] - x + 1):
                    for height in range(1, matrix.shape[1] - y + 1):
                        yield matrix[x:x + width, y:y + height]
    submatrices = []
    for submat in all_submatrices(matrix):
        if submat.sum() == -36:
            submatrices.append(submat)
    return submatrices