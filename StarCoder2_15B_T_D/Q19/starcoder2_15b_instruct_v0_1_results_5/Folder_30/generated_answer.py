def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 20 and i < 35 and (x % -36 != 0)]