def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst[:3]) if i in [0, 2] and x % 2 == 0]