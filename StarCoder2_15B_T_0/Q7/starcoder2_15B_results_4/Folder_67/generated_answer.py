def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 22 and i <= 50 and (x % 2 == 0)]