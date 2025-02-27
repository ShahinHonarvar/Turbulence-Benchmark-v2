def all_even_ints_exclusive(ints):
    return [num for i, num in enumerate(ints) if i >= 8 and i < 9 and (num % 2 == 0)]