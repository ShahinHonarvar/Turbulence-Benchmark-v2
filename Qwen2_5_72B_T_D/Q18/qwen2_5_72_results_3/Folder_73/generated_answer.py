def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[81:87]) if num % -33 == 0 or num % -62 == 0))