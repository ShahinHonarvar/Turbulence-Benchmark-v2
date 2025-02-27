import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(arr, n):
        count = 0
        rows, cols = arr.shape
        for i in range(rows):
            for j in range(cols):
                try:
                    if arr[i:i + int(n ** 0.5), j:j + int(n ** 0.5)].size == n:
                        count += 1
                except:
                    continue
        return count
    return count_submatrices_with_n_elements(matrix, 154)