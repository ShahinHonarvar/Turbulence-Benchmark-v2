def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst[30:88]) if i % 2 == 0 and x % 2 == 0]