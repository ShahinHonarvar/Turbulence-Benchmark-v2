def all_odd_ints_inclusive(int_list):
    return [x for i, x in enumerate(int_list) if i >= 13 and i <= 68 and (x % 2 == 1)]