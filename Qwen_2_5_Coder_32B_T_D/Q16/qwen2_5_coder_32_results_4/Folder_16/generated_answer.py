def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 33 and i <= 36 and (x % 2 == 0))) if len(lst) > 36 else 0