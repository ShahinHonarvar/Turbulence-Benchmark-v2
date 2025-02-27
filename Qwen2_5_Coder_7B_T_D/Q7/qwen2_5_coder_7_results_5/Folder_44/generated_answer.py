def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 13 and i <= 68 and (x % 2 == 0)]