def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if x % 93 == 0 and i in (52, 53)]