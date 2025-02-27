def sum_ints_div_by_either_nums(numbers):
    return sum((number for i, number in enumerate(numbers[55:85]) if number % -24 == 0 or number % -11 == 0))