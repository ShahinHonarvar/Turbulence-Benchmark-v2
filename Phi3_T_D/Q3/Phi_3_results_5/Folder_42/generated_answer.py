def all_pos_ints_inclusive(int_list):
    return [x for i, x in enumerate(int_list) if i in range(29, 80) and x > 0]