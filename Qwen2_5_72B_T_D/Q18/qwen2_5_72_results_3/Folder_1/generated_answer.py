def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[10:29]) if num % -61 == 0 or num % -64 == 0))