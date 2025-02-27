def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[14:94]) if num % 71 == 0 or num % 81 == 0))