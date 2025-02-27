import numpy as np

def submatrix_with_particular_sum(matrix):
    top = 0
    left = 0
    bottom = matrix.shape[0]
    right = matrix.shape[1]
    target_sum = 100
    submatrices = []
    while top < bottom:
        while left < right:
            temp = matrix[top:bottom, left:right].sum()
            if temp == target_sum:
                submatrices.append(matrix[top:bottom, left:right])
            if temp < target_sum:
                if right < matrix.shape[1]:
                    right += 1
                else:
                    right = matrix.shape[1]
            else:
                left += 1
        left = 0
        top += 1
    return submatrices