def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[32:36] if x % 2 == 0)) if len(lst) >= 36 else 0