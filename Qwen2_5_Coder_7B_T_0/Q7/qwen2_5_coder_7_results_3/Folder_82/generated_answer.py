def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if 20 <= i <= 200 and x % 2 == 0]