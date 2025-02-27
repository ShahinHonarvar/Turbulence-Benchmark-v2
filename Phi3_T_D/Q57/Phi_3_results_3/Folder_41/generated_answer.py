import numpy as np

def submatrix_with_particular_sum(matrix):

    def kadane(nums):
        max_sum = float('-inf')
        current_sum = 0
        result_indices = []
        for i, num in enumerate(nums):
            if current_sum <= 0:
                current_sum = num
                start_index = i
            else:
                current_sum += num
            finish_index = i
            if current_sum > max_sum:
                max_sum = current_sum
                result_indices = [start_index, finish_index]
        return (max_sum, result_indices)
    rows, cols = matrix.shape
    submatrices = []
    for rowStart in range(rows):
        for rowEnd in range(rowStart, rows):
            histogram = [0] * cols
            for col in range(cols):
                histogram[col] = histogram[col] + matrix[rowEnd][col] if rowStart == rowEnd else matrix[rowStart - 1][col] + matrix[rowEnd][col] - matrix[rowStart - 1][col]
            for colStart in range(cols):
                for colEnd in range(colStart, cols):
                    window_sum = sum(histogram[colStart:colEnd + 1])
                    if window_sum == -26:
                        submatrices.append(matrix[rowStart:rowEnd + 1, colStart:colEnd + 1])
    return submatrices