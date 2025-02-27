def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if 100 <= i <= 200 and x % 2 == 0]