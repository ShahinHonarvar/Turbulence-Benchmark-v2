def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if not 19 < i < 49 or x % -36 != 0]