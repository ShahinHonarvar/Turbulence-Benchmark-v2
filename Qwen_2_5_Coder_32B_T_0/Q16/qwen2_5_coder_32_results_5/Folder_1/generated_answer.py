def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 31 <= i <= 72 and x % 2 == 0)) if len(lst) > 72 else 0