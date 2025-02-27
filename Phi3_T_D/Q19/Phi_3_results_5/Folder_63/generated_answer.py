def all_ints_not_div_by_num(int_list):
    return [elem for idx, elem in enumerate(int_list[20:43]) if elem % 95 != 0]