def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[51:77]) if num % -90 == 0 or num % -59 == 0))