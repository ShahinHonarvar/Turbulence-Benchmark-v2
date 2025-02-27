def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[1:9], start=1) if num % -9 == 0 or num % -3 == 0))