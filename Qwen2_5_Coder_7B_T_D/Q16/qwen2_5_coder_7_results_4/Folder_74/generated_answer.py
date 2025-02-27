def sum_even_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers) if 17 <= i <= 78 and num % 2 == 0))