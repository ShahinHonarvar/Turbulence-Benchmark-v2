def all_ints_not_div_by_num(int_list):
    return [n for i, n in enumerate(int_list) if i >= 266 and i < 586 and (n % 840 != 0)]