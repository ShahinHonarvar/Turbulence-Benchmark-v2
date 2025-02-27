def all_even_ints_exclusive(numbers):
    even_ints = [num for i, num in enumerate(numbers) if i > 0 and i < 6 and (num % 2 == 0)]
    return even_ints