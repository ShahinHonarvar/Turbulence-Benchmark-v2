def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers) if i >= 11 and i <= 46 and (num % 55 == 0 or num % 36 == 0)))