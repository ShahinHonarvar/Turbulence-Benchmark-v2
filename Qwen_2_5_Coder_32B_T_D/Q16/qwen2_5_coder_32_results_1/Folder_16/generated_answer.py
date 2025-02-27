def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 33 <= i <= 36 and x % 2 == 0)) if len(lst) >= 37 else 0