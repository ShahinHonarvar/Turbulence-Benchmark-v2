def all_odd_ints_inclusive(int_list):
    return [x for i, x in enumerate(int_list) if i >= 10 and i <= 66 and (x % 2 == 1)]