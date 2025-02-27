def all_even_ints_exclusive(integers):
    return [num for i, num in enumerate(integers) if i > 11 and i < 76 and (num % 2 == 0)]