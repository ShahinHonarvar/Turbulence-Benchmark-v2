def all_odd_ints_inclusive(lst):
    return [x for x in lst[310:371] if x % 2 != 0] if len(lst) > 370 else []