def sum_even_ints_inclusive(ints):
    return sum((x for i, x in enumerate(ints) if 15 <= i <= 39 and x % 2 == 0)) if len(ints) > 39 else 0