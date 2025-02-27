import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(i, rows):
            temp = np.zeros(cols)
            for k in range(cols):
                temp[k] += matrix[j][k]
                if i > 0:
                    temp[k] += temp[k - 1]
                current_sum = 0
                start = 0
                for l in range(cols):
                    current_sum += temp[l]
                    if current_sum == -86:
                        result.append(matrix[i:j + 1, start:l + 1])
                    if current_sum > -86:
                        current_sum -= temp[start]
                        start += 1
    return result