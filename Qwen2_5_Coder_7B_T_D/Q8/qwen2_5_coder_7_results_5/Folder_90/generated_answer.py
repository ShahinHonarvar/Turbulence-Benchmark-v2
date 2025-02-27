def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 389 and i < 748 and (x % 2 == 0)]