def all_odd_ints_exclusive(lst):
    if len(lst) < 91:
        return []
    return [x for x in lst[67:90] if x % 2 != 0]