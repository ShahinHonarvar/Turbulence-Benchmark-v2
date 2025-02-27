def all_ints_not_div_by_num(int_list):
    return [val for idx, val in enumerate(int_list[10:55]) if val % 36 != 0]