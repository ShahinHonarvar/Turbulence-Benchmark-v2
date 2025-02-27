def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 62 <= i <= 92 and x % 2 == 0)) if len(lst) > 92 else 0