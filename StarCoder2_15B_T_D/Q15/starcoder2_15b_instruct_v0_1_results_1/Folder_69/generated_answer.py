def sum_odd_ints_inclusive(numbers):
    return sum((number for index, number in enumerate(numbers) if index >= 32 and index <= 35 and (number % 2 == 1)))