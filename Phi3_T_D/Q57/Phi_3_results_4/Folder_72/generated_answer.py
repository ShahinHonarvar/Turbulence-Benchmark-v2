import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape[:2]
    result = []

    def recursive_find(submat, i, j, current_sum, elements_count):
        if i == rows:
            return
        if j == cols:
            if current_sum == 41:
                result.append(submat.copy())
            return
        recursive_find(submat, i + 1, j, current_sum + matrix[i][j], elements_count + 1)
        if elements_count > 0:
            recursive_find(submat, i + 1, j + 1, current_sum, elements_count)
            recursive_find(submat, i, j + 1, current_sum + matrix[i][j], elements_count + 1)
    recursive_find([], 0, 0, 0, 0)
    return result