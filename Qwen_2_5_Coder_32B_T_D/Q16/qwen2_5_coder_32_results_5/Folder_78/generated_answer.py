def sum_even_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers) if 43 <= i <= 51 and num % 2 == 0))