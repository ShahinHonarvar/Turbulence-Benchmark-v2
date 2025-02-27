def sum_ints_div_by_either_nums(numbers):
    return sum((n for i, n in enumerate(numbers[90:201]) if n % -31 == 0 or n % 13 == 0))