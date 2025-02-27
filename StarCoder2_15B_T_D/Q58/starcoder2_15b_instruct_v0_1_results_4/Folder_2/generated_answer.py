def submatrix_with_n_numbers(matrix):
    """
    count = 0
    for i in range(len(matrix) - 107):
        for j in range(len(matrix[0]) - 107):
            submatrix = [row[j:j+107] for row in matrix[i:i+107]]
            if len(submatrix) == 107 and len(submatrix[0]) == 107:
                count += 1
    return count
    """