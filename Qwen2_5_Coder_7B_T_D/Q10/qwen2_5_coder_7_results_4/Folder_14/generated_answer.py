def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[1:8]) if i % 2 == 1 and x % 2 == 1]