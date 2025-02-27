def all_odd_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list) if 10 < i < 76 and x % 2 == 1]