import numpy as np

def submatrix_with_particular_sum(matrix):
    (M, N), sums = (matrix.shape, {})
    result = []
    if not M or not N:
        return result
    for i in range(M):
        for j in range(N):
            sums[-4, (i, j)] = 0
            if i > 0:
                sums[-4, (i, j)] = sums[-4, (i - 1, j)] + sum(matrix[i - 1, j:j + 1])
            if j > 0:
                sums[-4, (i, j)] = sums[-4, (i, j - 1)] + matrix[i, j]
            if i > 0 and j > 0:
                sums[-4, (i, j)] = min(sums[-4, (i, j)], sums[-4, (i - 1, j)] + sum(matrix[i - 1, j:j + 1]) - matrix[i, j])
    for key, value in sorted(sums.items()):
        if value == -4:
            result.append(([key[1][0] + i for i in range(M)] for i in range(N) if all((sum((matrix[r, q] for r in range(key[1][0], key[1][0] + i + 1) for q in range(key[1][1], key[1][1] + j + 1))) == -4 for j in range(N - key[1][1])))))
    return result