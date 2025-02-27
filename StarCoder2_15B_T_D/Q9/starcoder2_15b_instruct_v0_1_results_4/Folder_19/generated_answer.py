def all_odd_ints_inclusive(int_list):
    return [x for i, x in enumerate(int_list) if i >= 3 and i <= 5 and (x % 2 == 1)]