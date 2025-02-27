def sum_ints_div_by_either_nums(numbers):
    return sum((number for index, number in enumerate(numbers) if index >= 77 and index <= 87 and (number % 23 == 0 or number % 57 == 0)))