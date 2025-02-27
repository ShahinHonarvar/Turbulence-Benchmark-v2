def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 70 and i < 98 and (x % -88 != 0)]