def all_odd_ints_inclusive(int_list):
    return [x for i, x in enumerate(int_list) if i >= 22 and i <= 63 and (x % 2 == 1)]