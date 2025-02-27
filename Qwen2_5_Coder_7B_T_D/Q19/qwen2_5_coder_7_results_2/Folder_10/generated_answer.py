def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i in range(86, 89) and x % -61 != 0]