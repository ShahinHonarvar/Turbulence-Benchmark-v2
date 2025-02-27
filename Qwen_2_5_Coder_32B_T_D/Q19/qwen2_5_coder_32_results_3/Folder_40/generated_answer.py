def all_ints_not_div_by_num(lst):
    return lst[1:2] if len(lst) > 2 and lst[1] % 1 != 0 else []