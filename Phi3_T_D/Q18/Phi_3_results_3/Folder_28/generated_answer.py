def sum_ints_div_by_either_nums(numbers):
    return sum((n for n in numbers[34:82] if n % 27 == 0 or n % 57 == 0))