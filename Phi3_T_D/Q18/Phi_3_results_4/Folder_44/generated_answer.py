def sum_ints_div_by_either_nums(numbers):
    return sum((n for n in numbers[25:71] if n % 74 == 0 or n % 15 == 0))