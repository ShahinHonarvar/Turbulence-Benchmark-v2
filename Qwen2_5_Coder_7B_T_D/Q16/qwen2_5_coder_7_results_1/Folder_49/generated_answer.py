def sum_even_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers) if 8 <= i <= 80 and num % 2 == 0))