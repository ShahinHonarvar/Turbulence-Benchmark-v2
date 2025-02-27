def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[48:77]) if num % -46 == 0 or num % -82 == 0))