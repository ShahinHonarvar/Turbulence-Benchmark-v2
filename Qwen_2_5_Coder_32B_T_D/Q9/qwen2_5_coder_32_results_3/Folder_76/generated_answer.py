def all_odd_ints_inclusive(lst):
    if len(lst) < 988:
        return []
    return [x for x in lst[686:988] if x % 2 != 0]