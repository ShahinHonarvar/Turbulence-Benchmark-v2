def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[28:33] if x % 2 == 0)) if len(lst) > 32 else 0