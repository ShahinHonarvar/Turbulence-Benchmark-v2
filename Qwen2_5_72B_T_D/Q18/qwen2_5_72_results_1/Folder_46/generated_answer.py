def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[11:47], start=11) if num % 55 == 0 or num % 36 == 0))