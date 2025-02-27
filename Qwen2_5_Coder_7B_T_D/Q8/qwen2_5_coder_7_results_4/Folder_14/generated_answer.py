def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[1:8]) if i % 2 == 0 and x % 2 == 0]