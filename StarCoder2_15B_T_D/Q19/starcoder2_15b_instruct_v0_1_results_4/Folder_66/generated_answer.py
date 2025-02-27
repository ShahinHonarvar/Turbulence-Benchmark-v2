def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i in range(84, 86) and x % 99 != 0]