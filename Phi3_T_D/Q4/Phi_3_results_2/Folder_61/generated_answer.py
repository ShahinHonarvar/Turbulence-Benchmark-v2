def all_pos_ints_exclusive(int_list):
    result = [x for x in int_list[0:8] if isinstance(x, int) and x > 0]
    return result