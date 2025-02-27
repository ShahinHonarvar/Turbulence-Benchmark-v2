def all_odd_ints_inclusive(my_list):
    return [x for i, x in enumerate(my_list) if i >= 28 and i <= 40 and (x % 2 == 1)]