def sum_ints_div_by_either_nums(numbers):
    return sum((n for n in numbers[:5] if n % 8 == 0 or n % -3 == 0))