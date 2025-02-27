def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[66:94] if x % 2 == 0)) if len(lst) > 93 else 0