def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 0 and i <= 6 and (x % 2 == 0)]