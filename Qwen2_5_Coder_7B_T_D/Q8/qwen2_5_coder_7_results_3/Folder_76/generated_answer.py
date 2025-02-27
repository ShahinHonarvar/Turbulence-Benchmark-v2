def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 361 and i < 643 and (num % 2 == 0)]