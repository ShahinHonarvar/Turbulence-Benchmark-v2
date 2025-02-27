def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[11:77], start=11) if x % -81 == 0 or x % -94 == 0))