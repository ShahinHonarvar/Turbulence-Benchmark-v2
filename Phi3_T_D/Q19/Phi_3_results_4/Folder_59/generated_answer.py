def all_ints_not_div_by_num(int_list):
    return [x for i, x in enumerate(int_list[8:9], start=8) if x % 8 != 0]