import numpy as np

def submatrix_with_n_numbers(matrix):
    target = 88
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == target:
                count += 1
    total_submatrices = rows * (rows + 1) // 2 * (cols * (cols + 1) // 2)
    submatrices_with_n_numbers = total_submatrices - count * (rows * cols - 1)
    return max(0, submatrices_with_n_numbers)

def check_function():
    matrix = np.array([[1, 2, 88], [4, 88, 6], [7, 8, 9]])
    result = submatrix_with_n_numbers(matrix)
    assert result == 0, 'Test case 1 failed'
    matrix2 = np.array([[88, 88, 88], [88, 88, 88], [88, 88, 88]])
    result2 = submatrix_with_n_numbers(matrix2)
    assert result2 == 0, 'Test case 2 failed'
    print('All test cases passed!')