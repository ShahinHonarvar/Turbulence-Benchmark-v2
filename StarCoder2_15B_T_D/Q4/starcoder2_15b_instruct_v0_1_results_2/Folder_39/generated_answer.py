def all_pos_ints_exclusive(lst):
    return [x for x in lst[43:99] if x > 0] if any((x > 0 for x in lst[43:99])) else []