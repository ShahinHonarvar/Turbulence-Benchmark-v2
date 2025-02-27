def all_ints_not_div_by_num(lst):
    return lst[91:200] if len(lst) > 200 else [x for x in lst[91:200] if x % -31 != 0]