def sum_ints_div_by_either_nums(lst):
    total = sum((val for val in lst[154:799] if val % 275 == 0 or val % 580 == 0))
    return total