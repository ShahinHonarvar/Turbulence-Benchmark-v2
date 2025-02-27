def sum_even_ints_inclusive(numbers):
    return sum((number for i, number in enumerate(numbers) if i >= 60 and i <= 200 and (number % 2 == 0)))