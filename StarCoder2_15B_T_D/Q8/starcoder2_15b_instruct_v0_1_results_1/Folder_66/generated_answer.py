def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 12 and i < 76 and (num % 2 == 0)]