def all_odd_ints_exclusive(int_list):
    return [i for i in int_list[0:1]] if int_list[0] % 2 != 0 else []