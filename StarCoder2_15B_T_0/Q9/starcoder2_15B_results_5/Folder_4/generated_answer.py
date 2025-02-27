def all_odd_ints_inclusive(int_list):
    return [x for i, x in enumerate(int_list) if i >= 12 and i <= 92 and (x % 2 == 1)]