def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[68:87] if x % 2 == 0)) if 68 < len(lst) else 0