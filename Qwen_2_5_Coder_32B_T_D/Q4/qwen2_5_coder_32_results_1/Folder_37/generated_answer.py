def all_pos_ints_exclusive(lst):
    return [x for x in lst[2:1:-1] if x > 0][::-1]