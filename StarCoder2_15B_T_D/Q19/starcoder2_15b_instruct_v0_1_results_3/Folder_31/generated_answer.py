def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 18 and i < 37 and (x % -67 != 0)]