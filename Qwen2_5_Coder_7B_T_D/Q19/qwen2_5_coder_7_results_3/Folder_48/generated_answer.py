def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i > 767 and i < 938 and (x % 593 != 0)]