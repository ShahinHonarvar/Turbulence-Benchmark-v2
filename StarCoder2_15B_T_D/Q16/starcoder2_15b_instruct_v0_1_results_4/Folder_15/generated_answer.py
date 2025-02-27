def sum_even_ints_inclusive(ints):
    even_ints = [i for i in ints if i % 2 == 0]
    return sum(even_ints[:4]) if len(even_ints) >= 4 else 0