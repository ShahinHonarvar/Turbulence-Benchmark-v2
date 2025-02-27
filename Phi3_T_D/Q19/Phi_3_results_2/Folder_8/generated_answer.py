def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst[17:88]) if x % -75 != 0]