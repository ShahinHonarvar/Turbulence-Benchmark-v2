def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if 1 <= i <= 8 and x % 2 == 0]