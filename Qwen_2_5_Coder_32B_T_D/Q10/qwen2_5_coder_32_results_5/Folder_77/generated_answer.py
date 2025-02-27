def all_odd_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list) if i > 111 and i < 473 and (x % 2 != 0)]