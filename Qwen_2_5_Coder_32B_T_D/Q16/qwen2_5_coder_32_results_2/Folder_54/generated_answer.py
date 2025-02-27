def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[34:56] if x % 2 == 0)) if 0 <= 34 < 56 <= len(lst) else 0