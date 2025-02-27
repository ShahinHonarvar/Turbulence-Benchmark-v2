def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 28 <= i <= 32 and x % 2 == 0)) if len(lst) > 32 else 0