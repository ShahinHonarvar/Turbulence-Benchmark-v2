def all_even_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if 3 <= i <= 5 and num % 2 == 0]