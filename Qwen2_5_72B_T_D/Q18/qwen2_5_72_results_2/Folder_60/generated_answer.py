def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[10:80], start=10) if num % -74 == 0 or num % -58 == 0))