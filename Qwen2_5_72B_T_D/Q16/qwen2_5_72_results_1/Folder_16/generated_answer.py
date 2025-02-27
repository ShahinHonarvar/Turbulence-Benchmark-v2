def sum_even_ints_inclusive(numbers):
    return sum((num for idx, num in enumerate(numbers) if 33 <= idx <= 36 and num % 2 == 0))