def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 1 and i <= 8 and (x % 2 == 0))) if len(lst) > 8 else sum((x for i, x in enumerate(lst) if i >= 1 and x % 2 == 0))