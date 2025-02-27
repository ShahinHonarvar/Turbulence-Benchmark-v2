def all_odd_ints_exclusive(lst):
    if len(lst) <= 767:
        return []
    return [x for x in lst[599:767] if x % 2 != 0]