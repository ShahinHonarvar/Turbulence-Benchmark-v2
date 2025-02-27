def all_odd_ints_inclusive(lst):
    if 6 < len(lst) - 1:
        return [x for x in lst[6:7] if x % 2 != 0]
    return []