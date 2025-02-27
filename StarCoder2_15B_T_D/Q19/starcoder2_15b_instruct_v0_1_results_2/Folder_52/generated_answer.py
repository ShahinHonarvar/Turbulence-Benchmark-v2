def all_ints_not_div_by_num(my_list):
    return [x for i, x in enumerate(my_list) if i >= 50 and i < 92 and (x % 16 != 0)]