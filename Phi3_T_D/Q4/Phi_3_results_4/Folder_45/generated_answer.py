def all_pos_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if 30 < i < 200 and num > 0]