def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 19 and i <= 92 and (x % 2 == 0)]