def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[32:100], start=32) if num % -11 == 0 or num % -15 == 0))