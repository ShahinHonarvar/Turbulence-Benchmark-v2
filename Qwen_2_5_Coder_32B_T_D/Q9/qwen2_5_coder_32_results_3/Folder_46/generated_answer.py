def all_odd_ints_inclusive(lst):
    if len(lst) < 88:
        return []
    return [x for x in lst[30:88] if x % 2 != 0]