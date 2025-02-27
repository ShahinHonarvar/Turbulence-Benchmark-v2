def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst, start=1) if 11 <= i <= 76 and (x % -81 == 0 or x % -94 == 0)))