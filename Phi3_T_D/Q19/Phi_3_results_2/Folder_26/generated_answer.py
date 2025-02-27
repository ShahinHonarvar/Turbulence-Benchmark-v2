def all_ints_not_div_by_num(int_list):
    return [x for i, x in enumerate(int_list[38:81]) if x % 49 != 0]