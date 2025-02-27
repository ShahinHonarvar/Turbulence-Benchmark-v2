def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[57:85]) if num % -30 == 0 or num % -88 == 0))