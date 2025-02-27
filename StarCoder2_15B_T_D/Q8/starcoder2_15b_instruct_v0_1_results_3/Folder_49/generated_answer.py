def all_even_ints_exclusive(ints):
    return [num for i, num in enumerate(ints) if i > 80 and i < 200 and (num % 2 == 0)]