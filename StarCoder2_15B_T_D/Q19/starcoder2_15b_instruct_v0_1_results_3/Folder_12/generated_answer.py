def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 59 and i < 93 and (x % -26 != 0)]