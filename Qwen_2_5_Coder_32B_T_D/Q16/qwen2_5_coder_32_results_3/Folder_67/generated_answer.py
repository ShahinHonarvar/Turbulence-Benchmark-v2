def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 22 <= i <= 50 and x % 2 == 0)) if len(lst) > 50 else 0