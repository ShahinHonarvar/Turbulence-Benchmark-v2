def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst, start=1) if 18 < i < 38 and x % -67 != 0]