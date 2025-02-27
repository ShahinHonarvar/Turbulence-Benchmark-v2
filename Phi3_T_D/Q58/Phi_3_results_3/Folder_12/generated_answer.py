import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    count_smaller_submat = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            count_smaller_submat = 1
            for k in range(i, rows):
                for l in range(j, cols):
                    count_smaller_submat += 1
                    if count_smaller_submat == 46:
                        count += 1
                        break
                if count_smaller_submat == 46:
                    break
    return count