def sum_ints_div_by_either_nums(numbers):
    return sum((n for i, n in enumerate(numbers[93:95], start=93) if n % -53 == 0 or n % -91 == 0))