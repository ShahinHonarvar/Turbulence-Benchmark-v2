def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if x % 2 == 0 and 0 < i < 4]