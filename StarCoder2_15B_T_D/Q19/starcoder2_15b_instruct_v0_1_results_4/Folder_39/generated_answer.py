def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 22 and i < 97 and (x % -46 != 0)]