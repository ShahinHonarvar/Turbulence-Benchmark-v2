def sum_even_ints_inclusive(numbers):
    return sum((num for index, num in enumerate(numbers) if 70 <= index <= 200 and num % 2 == 0))