def all_odd_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list) if i % 2 == 1 and 28 <= i < 53]