def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 2 and i < 7 and (num % 2 == 0)]