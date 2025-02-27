def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 17 and i <= 78 and (x % 2 == 0)]