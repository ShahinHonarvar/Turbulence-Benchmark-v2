def sum_ints_div_by_either_nums(numbers):
    return sum((n for i, n in enumerate(numbers) if i >= 57 and i <= 84 and (n % -30 == 0) or n % -88 == 0))