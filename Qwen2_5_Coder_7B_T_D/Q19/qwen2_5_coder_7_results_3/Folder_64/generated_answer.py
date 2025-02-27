def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i not in [2, 3] and x % 2 != 0]