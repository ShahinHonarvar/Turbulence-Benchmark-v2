def all_even_ints_exclusive(numbers):
    return [n for i, n in enumerate(numbers[28:52], start=28) if n % 2 == 0]