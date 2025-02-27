import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    target_sum = -43
    result = []

    def kadane(arr):
        max_ending_here = max_so_far = 0
        for x in arr:
            max_ending_here += x
            if max_ending_here < 0:
                max_ending_here = 0
            elif max_ending_here > max_so_far:
                max_so_far = max_ending_here
        return max_so_far
    for size in range(1, min(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if kadane(submatrix.flatten()) == target_sum:
                    result.append(submatrix.tolist())
    return result