def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 8 <= i <= 80 and x % 2 == 0)) if len(lst) > 80 else 0