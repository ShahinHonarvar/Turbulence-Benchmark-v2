def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 42 <= i <= 68 and x % 2 == 0)) if len(lst) > 68 else 0