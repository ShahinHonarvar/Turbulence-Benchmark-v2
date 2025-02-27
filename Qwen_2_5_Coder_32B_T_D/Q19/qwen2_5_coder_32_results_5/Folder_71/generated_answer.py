def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 21 < i < 51 and x % -77 != 0]