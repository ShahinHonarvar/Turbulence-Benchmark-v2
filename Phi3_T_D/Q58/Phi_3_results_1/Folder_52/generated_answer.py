import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            num = 0
            for x in range(i, size):
                for y in range(j, size):
                    num += sum((matrix[x_i][y] for x_i in range(x, x + (x - i) + 1) for y in range(y, y + (y - j) + 1)))
                    if num == 147:
                        count += 1
                    if num > 147:
                        break
                if num > 147:
                    break
    return count