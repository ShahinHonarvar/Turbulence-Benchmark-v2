def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst[1:6]) if x % -6 != 0]