def all_odd_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list) if 19 < i < 94 and x % 2 == 1]