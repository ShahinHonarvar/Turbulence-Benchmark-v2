def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst[199:202]) if x % -200 != 0]