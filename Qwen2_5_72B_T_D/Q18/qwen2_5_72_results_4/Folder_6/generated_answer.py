def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[41:57]) if num % 82 == 0 or num % 90 == 0))