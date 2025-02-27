def all_odd_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list) if 43 <= i < 99 and x % 2 != 0]