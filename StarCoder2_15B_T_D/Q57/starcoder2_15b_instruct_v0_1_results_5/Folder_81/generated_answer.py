import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            submatrix = np.array([[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]])
            if sum(submatrix.flatten()) == -90:
                result.append(submatrix)
    return result

def main():
    matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    result = submatrix_with_particular_sum(matrix)
    print(result)