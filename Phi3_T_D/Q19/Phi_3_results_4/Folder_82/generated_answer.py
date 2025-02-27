def all_ints_not_div_by_num(lst):
    return [item for index, item in enumerate(lst[20:200]) if item % -200 != 0]