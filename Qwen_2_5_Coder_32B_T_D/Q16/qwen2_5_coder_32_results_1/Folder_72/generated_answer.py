def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[29:52] if x % 2 == 0)) if len(lst) > 51 else 0