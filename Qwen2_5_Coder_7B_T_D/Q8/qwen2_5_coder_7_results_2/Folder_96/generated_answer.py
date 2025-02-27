def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if 50 < i < 200 and num % 2 == 0]