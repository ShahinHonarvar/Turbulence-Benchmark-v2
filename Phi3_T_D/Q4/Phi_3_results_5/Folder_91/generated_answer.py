def all_pos_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list[0:5]) if 0 < x]