def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[55:85]) if num % -24 == 0 or num % -11 == 0))