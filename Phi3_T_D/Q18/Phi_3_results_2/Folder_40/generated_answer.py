def sum_ints_div_by_either_nums(numbers):
    return sum((n for n in numbers[:2] if n % 2 == 0 or n % 1 == 0))