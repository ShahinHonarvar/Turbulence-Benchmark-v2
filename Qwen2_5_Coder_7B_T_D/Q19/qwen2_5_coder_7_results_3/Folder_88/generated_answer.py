def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst[4:7]) if x % -6 != 0]