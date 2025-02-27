def all_ints_div_by_num(int_list):
    return [x for x in int_list if x % 9 == 0 and 0 <= int_list.index(x) <= 0]