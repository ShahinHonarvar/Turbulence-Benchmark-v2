def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 30 < i < 200 and x % -115 != 0]