def all_pos_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list) if 1 < i < 7 and x > 0]