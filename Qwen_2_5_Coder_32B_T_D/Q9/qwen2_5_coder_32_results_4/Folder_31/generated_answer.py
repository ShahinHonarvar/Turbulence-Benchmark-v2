def all_odd_ints_inclusive(lst):
    if len(lst) < 89:
        return []
    return [x for x in lst[75:89] if x % 2 != 0]