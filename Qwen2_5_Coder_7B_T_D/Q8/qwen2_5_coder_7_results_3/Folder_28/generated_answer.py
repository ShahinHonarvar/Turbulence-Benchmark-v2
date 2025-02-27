def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers, start=1) if 20 < i < 52 and num % 2 == 0]