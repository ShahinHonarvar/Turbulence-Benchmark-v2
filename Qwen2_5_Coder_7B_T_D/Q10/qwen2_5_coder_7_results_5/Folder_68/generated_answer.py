def all_odd_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list) if i > 0 and i < 9 and (x % 2 != 0)]