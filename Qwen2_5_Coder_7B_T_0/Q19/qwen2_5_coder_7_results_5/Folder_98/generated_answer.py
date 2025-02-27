def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i not in range(1, 6) and x % 13 != 0]