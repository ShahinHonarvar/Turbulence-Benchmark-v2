def sum_ints_div_by_either_nums(numbers):
    return sum((number for i, number in enumerate(numbers) if i >= 58 and i <= 75 and (number % 72 == 0 or number % 62 == 0)))