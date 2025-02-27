def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst[38:81]) if x % 49 != 0]