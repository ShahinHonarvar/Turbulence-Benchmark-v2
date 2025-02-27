def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 70 <= i <= 84 and x % 2 == 0)) if len(lst) > 84 else 0