def all_odd_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list) if i >= 38 and i < 77 and (x % 2 == 1)]