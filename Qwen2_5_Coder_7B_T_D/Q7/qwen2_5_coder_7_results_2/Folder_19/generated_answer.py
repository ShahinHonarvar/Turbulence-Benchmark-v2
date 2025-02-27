def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if 3 <= i <= 5 and x % 2 == 0]