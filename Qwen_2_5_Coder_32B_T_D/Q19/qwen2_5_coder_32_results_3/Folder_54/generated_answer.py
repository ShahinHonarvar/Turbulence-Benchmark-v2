def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 19 < i < 94 and x % -32 != 0]