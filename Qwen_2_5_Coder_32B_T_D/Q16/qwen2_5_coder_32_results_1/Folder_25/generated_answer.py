def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 29 <= i <= 93 and x % 2 == 0)) if len(lst) > 93 else 0