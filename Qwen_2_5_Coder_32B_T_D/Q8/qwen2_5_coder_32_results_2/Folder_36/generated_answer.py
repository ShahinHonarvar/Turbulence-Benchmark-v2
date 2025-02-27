def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 598 and i < 767 and (x % 2 == 0)]