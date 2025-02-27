def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i in range(6, 9) and x % -9 == 0]