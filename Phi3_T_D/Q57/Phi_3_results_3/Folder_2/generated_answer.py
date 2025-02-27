import numpy as np

def submatrix_with_particular_sum(matrix):

    def count_submatrix(matrix, target_sum=-863):
        rows, cols = matrix.shape
        count = 0
        for left in range(cols):
            temp_sum = [0] * rows
            for right in range(left, cols):
                for i in range(rows):
                    temp_sum[i] += matrix[i][right]
                sum_submatrix = {0: []}
                for i in range(rows):
                    if temp_sum[i] in sum_submatrix:
                        submatrices = sum_submatrix[temp_sum[i]]
                        for sub in submatrices:
                            start_row, end_row = sub
                            sum_submatrix[temp_sum[i] - sum_submatrix[target_sum]] = sum_submatrix.get(temp_sum[i] - sum_submatrix[target_sum], []) + [(start_row, i)]
                    else:
                        sum_submatrix[temp_sum[i]] = []
                    if temp_sum[i] - target_sum in sum_submatrix:
                        sum_submatrix[temp_sum[i]] += [(sum_submatrix[temp_sum[i] - target_sum][-1][1] + 1, i)]
                for sub in sum_submatrix.get(target_sum, []):
                    for start_row, end_row in sum_submatrix.get(target_sum, []):
                        if start_row >= sub[0] and end_row <= sub[1]:
                            yield matrix[start_row:end_row + 1, left:right + 1]
        return count
    return [submat for submat in count_submatrix(matrix)]