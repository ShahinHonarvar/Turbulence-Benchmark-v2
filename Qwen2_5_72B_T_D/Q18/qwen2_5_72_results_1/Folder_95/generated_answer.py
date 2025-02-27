def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[57:85] if x % -30 == 0 or x % -88 == 0)) if len(lst) > 84 else 0