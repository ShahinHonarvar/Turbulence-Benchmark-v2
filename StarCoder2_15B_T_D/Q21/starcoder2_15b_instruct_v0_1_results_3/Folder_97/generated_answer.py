def all_ints_div_by_num(ints_list):
    return [x for i, x in enumerate(ints_list) if i >= 17 and i <= 63 and (x % 89 == 0)]