def all_odd_ints_exclusive(lst):
    start, end = (93, 94)
    return [x for x in lst[start:end] if x % 2 != 0]