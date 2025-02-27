def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 74 <= i <= 95 and x % 2 == 0)) if len(lst) > 95 else 0