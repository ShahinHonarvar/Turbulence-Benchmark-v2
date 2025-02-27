def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[306:958]) if num % 982 == 0 or num % 319 == 0))