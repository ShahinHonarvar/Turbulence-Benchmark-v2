def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 27 and i <= 55 and (x % 2 == 0)]