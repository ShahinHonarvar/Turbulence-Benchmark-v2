def is_valid_submatrix(matrix):
    return len(matrix) == len(matrix[0]) == 126

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 125):
        for j in range(len(matrix[0]) - 125):
            submatrix = [row[j:j + 126] for row in matrix[i:i + 126]]
            if is_valid_submatrix(submatrix):
                count += 1
    return count