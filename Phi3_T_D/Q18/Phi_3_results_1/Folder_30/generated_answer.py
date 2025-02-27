def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[10:76]) if x % -81 == 0 or x % -94 == 0))