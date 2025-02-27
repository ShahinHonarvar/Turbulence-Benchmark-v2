def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 6 and i < 9 and (num % 2 == 0)]