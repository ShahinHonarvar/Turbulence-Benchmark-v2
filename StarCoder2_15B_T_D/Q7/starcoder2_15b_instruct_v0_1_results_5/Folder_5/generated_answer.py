def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 8 and i <= 9 and (x % 2 == 0)]