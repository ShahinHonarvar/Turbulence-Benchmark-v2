def all_even_ints_exclusive(integers):
    if len(integers) < 78:
        raise ValueError('List is too short.')
    return [n for i, n in enumerate(integers) if i >= 38 and i < 77 and (n % 2 == 0)]