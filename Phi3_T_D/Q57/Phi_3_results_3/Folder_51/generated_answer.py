import numpy as np

def submatrix_with_particular_sum(matrix):

    def count_submatrix(top, left, bottom, right, matrix):
        if bottom > matrix.shape[0] or right > matrix.shape[1]:
            return ([], float('inf'))
        current_sum = np.sum(matrix[top:bottom + 1, left:right + 1])
        total_count = 1 if current_sum == -46 else 0
        left_sum, right_sum = count_submatrix(top, left + 1, bottom, right, matrix)
        right_sum += current_sum
        return (left_sum + right_sum, total_count)
    total_count = 0
    all_submatrices = []
    for top in range(matrix.shape[0]):
        for left in range(matrix.shape[1]):
            bottom_sum, left_count = count_submatrix(top, left, matrix.shape[0] - 1, matrix.shape[1] - 1, matrix)
            all_count = left_count + bottom_sum
            total_count += all_count
            if all_count > 0:
                all_submatrices.extend(generate_submatrices(top, left, matrix.shape[0] - 1, matrix.shape[1] - 1))
    return all_submatrices if total_count > 1 else []

def generate_submatrices(top, left, bottom, right):
    if left == right:
        return [[[top, left], [bottom, right]]]
    else:
        median = (left + right) // 2
        left_sub = generate_submatrices(top, left, median, right)
        right_sub = generate_submatrices(top, median + 1, bottom, right)
        return left_sub + right_sub