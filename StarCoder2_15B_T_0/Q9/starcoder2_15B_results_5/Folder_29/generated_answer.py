def all_odd_ints_inclusive(int_list):
    return [x for i, x in enumerate(int_list) if i >= 59 and i <= 97 and (x % 2 == 1)]