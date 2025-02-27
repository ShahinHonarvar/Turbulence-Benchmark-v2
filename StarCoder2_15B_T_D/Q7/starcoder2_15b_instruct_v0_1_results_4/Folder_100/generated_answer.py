def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 42 and i <= 68 and (x % 2 == 0)]