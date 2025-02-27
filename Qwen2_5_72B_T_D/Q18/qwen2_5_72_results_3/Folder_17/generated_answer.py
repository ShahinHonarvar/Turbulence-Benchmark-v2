def sum_ints_div_by_either_nums(numbers):
    return sum((numbers[81:90:1][i] for i in range(9) if numbers[81:90:1][i] % 56 == 0 or numbers[81:90:1][i] % 68 == 0))