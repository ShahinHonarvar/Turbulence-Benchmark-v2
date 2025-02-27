def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 18 and i < 60 and (num % 2 == 0)]