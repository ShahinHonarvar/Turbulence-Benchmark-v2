def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[48:60]) if num % 88 == 0 or num % 58 == 0))