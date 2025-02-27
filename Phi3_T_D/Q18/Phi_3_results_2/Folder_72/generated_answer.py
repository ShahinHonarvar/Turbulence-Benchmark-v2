def sum_ints_div_by_either_nums(numbers):
    return sum((n for i, n in enumerate(numbers[38:82], start=38) if n % -61 == 0 or n % -71 == 0))