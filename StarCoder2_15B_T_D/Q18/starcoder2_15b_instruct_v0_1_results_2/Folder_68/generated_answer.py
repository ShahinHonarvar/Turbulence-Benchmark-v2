def sum_ints_div_by_either_nums(numbers):
    return sum((number for index, number in enumerate(numbers) if (number % 5 == 0 or number % 7 == 0) and 7 <= index <= 7))