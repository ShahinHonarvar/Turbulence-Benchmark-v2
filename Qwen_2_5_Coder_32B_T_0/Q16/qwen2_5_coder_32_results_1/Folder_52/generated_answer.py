def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 28 <= i <= 38 and x % 2 == 0)) if len(lst) > 38 else 0