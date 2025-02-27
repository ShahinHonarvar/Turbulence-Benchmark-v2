def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 667 <= i <= 774 and x % 2 == 0)) if len(lst) > 774 else 0