def sum_ints_div_by_either_nums(numbers):
    return sum((n for i, n in enumerate(numbers[14:94], start=14) if n % 71 == 0 or n % 81 == 0))