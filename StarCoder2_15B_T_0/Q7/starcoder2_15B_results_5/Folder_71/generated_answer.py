def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 26 and i <= 52 and (x % 2 == 0)]