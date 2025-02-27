def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[3:10], start=3) if num % 6 == 0 or num % 1 == 0))