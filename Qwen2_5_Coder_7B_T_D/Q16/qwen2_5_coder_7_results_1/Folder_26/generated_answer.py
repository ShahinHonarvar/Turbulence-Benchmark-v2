def sum_even_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers) if 62 <= i <= 99 and num % 2 == 0))