def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[40:200]) if i % 2 != 0 and x % 2 != 0]