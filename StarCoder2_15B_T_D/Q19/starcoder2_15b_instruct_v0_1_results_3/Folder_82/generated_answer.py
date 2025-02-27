def all_ints_not_div_by_num(ints_list):
    return [n for i, n in enumerate(ints_list) if i >= 20 and i < 200 and (n % -200 != 0)]