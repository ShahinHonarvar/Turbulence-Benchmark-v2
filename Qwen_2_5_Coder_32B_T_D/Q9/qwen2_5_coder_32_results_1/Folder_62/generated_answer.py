def all_odd_ints_inclusive(lst):
    if len(lst) < 100:
        return []
    return [x for x in lst[91:100] if x % 2 != 0]