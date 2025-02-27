def all_ints_div_by_num(ints_list):
    return [x for i, x in enumerate(ints_list) if i >= 45 and i <= 80 and (x % 39 == 0)]