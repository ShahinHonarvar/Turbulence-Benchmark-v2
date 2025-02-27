def all_pos_ints_exclusive(lst):
    if not lst or len(lst) < 100:
        return []
    return [x for x in lst[10:100] if x > 0]