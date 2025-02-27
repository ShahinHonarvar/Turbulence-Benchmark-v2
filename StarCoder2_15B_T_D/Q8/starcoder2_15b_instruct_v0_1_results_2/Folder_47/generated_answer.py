def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i % 2 == 0 and 64 <= i < 80]