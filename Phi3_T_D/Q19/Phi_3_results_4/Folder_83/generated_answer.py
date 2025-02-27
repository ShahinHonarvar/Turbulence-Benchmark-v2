def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst[90:200]) if x % -31 != 0]