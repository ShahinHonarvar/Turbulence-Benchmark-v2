def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 36 and i < 85 and (num % 2 == 0)]