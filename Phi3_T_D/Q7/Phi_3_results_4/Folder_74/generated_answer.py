def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i in range(17, 79) and x % 2 == 0]