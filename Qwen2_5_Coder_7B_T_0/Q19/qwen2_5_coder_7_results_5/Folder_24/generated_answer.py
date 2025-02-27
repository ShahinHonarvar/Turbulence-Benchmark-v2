def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 41 < i < 69 and x % -82 != 0]