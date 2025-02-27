def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 40 and i <= 80 and (x % 2 == 0)]