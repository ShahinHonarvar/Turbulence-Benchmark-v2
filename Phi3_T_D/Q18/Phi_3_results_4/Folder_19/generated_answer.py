def sum_ints_div_by_either_nums(numbers):
    return sum((n for i, n in enumerate(numbers[1:5], start=1) if n % 4 == 0 or n % -6 == 0))