def all_odd_ints_inclusive(lst):
    if len(lst) < 606:
        return []
    return [x for x in lst[533:606] if x % 2 != 0]