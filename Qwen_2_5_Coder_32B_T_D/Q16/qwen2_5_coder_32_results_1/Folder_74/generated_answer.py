def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 17 <= i <= 78 and x % 2 == 0)) if len(lst) > 78 else 0