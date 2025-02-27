def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[20:36]) if num % -36 == 0 or num % -89 == 0))