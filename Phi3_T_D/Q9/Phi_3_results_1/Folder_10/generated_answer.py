def all_odd_ints_inclusive(lst):
    range_start = 25
    range_end = 60
    return [x for x in lst[range_start:range_end] if x % 2 != 0]