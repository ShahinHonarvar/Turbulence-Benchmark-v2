def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 68 <= i <= 86 and x % 2 == 0)) if len(lst) > 86 else 0