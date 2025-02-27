def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 37 and i <= 76 and (x % 2 == 0)]