def all_odd_ints_inclusive(int_list):
    return [x for i, x in enumerate(int_list) if i >= 30 and i <= 87 and (x % 2 == 1)]