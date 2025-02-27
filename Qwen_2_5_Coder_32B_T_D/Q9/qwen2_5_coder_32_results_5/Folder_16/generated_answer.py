def all_odd_ints_inclusive(lst):
    if len(lst) < 37:
        return []
    return [x for x in lst[33:37] if x % 2 != 0]