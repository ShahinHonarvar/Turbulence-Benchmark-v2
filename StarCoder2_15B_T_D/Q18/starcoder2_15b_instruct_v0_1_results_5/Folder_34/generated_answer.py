def sum_ints_div_by_either_nums(numbers):
    return sum((n for n in numbers[60:201] if n % 9 == 0 or n % 11 == 0))