def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 56 <= i <= 82 and x % 2 == 0)) if len(lst) > 82 else 0