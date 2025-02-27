def all_ints_div_by_num(int_list):
    return [x for i, x in enumerate(int_list) if i >= 30 and i <= 59 and (x % 39 == 0)]