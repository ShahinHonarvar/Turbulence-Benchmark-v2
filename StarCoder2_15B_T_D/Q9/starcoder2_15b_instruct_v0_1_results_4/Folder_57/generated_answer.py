def all_odd_ints_inclusive(int_list):
    return [x for i, x in enumerate(int_list) if i >= 27 and i <= 55 and (x % 2 == 1)]