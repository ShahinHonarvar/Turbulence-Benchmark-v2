def all_pos_ints_inclusive(int_list):
    return [x for i, x in enumerate(int_list) if 26 <= i <= 52 and x > 0]