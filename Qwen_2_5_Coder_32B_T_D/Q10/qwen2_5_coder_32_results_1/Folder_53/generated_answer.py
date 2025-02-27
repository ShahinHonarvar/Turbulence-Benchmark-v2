def all_odd_ints_exclusive(lst):
    if len(lst) > 101:
        return [x for x in lst[101:102] if x % 2 != 0]
    return []