def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 22 <= i <= 88 and x % 2 == 0)) if len(lst) > 88 else 0