def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 246 <= i <= 750 and x % 2 == 0)) if len(lst) > 750 else 0