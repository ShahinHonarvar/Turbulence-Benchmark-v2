import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_subarrays_with_sum(arr, target):
        n = len(arr)
        result = []
        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += arr[end]
                if current_sum == target:
                    result.append((start, end))
        return result
    rows, cols = matrix.shape
    result_submatrices = []
    for left in range(cols):
        for right in range(left, cols):
            column_sums = np.sum(matrix[:, left:right + 1], axis=1)
            subarrays = find_subarrays_with_sum(column_sums, -157)
            for top, bottom in subarrays:
                result_submatrices.append(matrix[top:bottom + 1, left:right + 1])
    return result_submatrices if result_submatrices else []