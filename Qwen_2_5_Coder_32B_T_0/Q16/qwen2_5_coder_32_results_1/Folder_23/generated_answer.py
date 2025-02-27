def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 52 <= i <= 71 and x % 2 == 0)) if len(lst) > 71 else 0