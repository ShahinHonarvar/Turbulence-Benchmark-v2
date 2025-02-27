import numpy as np

def submatrix_with_particular_sum(matrix):
    size = len(matrix)
    sums = {0: [(0, 0)]}
    top, left = (0, 0)
    submatrices = []
    for i in range(size):
        right = 0
        for j in range(size):
            top_sum = 0
            while top_sum < 87 and top <= i:
                left_sum = 0
                for k in range(left, size):
                    left_sum += matrix[top][k]
                    if left_sum == 87:
                        submatrices.append(((top, left), (i, k)))
                    if top_sum + left_sum == 87:
                        for l in range(left, k + 1):
                            top_sum += matrix[top][l]
                            sums[top_sum - 87].append(((top + 1, left + 1), (i, k)))
                        break
                if left_sum == 87:
                    submatrices.append(((top, left), (i, size - 1)))
                left = k + 1
            top_sum += matrix[i][j]
            if top_sum not in sums:
                sums[top_sum] = []
            sums[top_sum].append(((i, j), (i, left)))
        right = size
        left = 0
        while sums.get(top_sum - 87):
            for bottom, upper in sums.get(top_sum - 87, []):
                if bottom == i:
                    submatrices.append(((top, upper), (i, j)))
            del sums[top_sum - 87]
        top = size
    return [np.array(matrix[i1:i2 + 1, j1:j2 + 1]) for (i1, j1), (i2, j2) in submatrices]