def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[2:8]) if num % -1 == 0 or num % -7 == 0))