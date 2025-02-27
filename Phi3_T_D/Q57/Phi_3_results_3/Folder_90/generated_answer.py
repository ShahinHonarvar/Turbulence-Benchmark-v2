import numpy as np

def submatrix_with_particular_sum(matrix):

    def helper(start_r, start_c, size, curr_submatrix, total_sum, result):
        if total_sum == -452:
            result.append(curr_submatrix)
            return
        if total_sum > -452 or (size == 1 and total_sum < -452):
            return
        curr_r, curr_c = (start_r, start_c)
        size += 1
        while curr_r < len(matrix) - size + 1:
            c_index = 0
            while c_index < len(matrix[0]):
                curr_sum += matrix[curr_r + (size - 1)][curr_c]
                c_index += 1
                if curr_sum == -452:
                    result.append(curr_submatrix + [row[curr_c:curr_c + size] for row in matrix[curr_r:curr_r + size]])
                    curr_sum -= matrix[curr_r + (size - 1)][curr_c]
                elif curr_sum < -452:
                    total_sum = curr_sum
                curr_c += 1
            curr_c -= c_index - 1
            curr_r += 1
            curr_submatrix.clear()
            curr_sum = 0
            total_sum = 0
    result = []
    curr_submatrix = []
    curr_sum = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            helper(r, c, 0, curr_submatrix, curr_sum, result)
    return result