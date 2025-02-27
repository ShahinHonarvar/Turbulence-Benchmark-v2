def sum_ints_div_by_either_nums(numbers):
    return sum((n for n in numbers[10:77] if n % -40 == 0 or n % -12 == 0))