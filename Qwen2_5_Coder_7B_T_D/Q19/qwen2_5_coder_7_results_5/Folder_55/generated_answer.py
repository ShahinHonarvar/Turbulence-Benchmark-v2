def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i not in range(10) and x % 10 != 0]