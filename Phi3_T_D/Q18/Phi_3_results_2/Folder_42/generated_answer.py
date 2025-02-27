def sum_ints_div_by_either_nums(numbers):
    return sum((n for i, n in enumerate(numbers[29:46], start=29) if n % 27 == 0 or n % 81 == 0))