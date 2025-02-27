def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 40 and i < 200 and (x % 71 != 0)]