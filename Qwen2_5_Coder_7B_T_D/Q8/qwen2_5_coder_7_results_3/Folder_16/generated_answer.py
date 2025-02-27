def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i in range(86, 90) and x % 2 == 0]