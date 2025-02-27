import numpy as np

def submatrix_with_particular_sum(matrix, target_sum=126):

    def search(x, y, size):
        nonlocal total
        if total == target_sum:
            result.append(matrix[x:x + size, y:y + size])
            return
        if total > target_sum:
            return
        if x + size > matrix.shape[0]:
            return
        for end_x in range(x + size, matrix.shape[0]):
            total += np.sum(matrix[x:end_x, y:y + size])
            search(end_x, y, size)
            total -= np.sum(matrix[x:end_x, y:y + size])
        if y + size < matrix.shape[1]:
            search(x, y + size, size)
    result = []
    size = 1
    total = 0
    while size <= min(matrix.shape):
        search(0, 0, size)
        size += 1
    return result