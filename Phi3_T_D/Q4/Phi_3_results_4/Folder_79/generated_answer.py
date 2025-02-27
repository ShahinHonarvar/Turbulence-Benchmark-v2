def all_pos_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list) if 3 < i < 8 and x > 0]