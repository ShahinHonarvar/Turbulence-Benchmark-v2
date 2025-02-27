def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if (i >= 30 and i <= 200) and (x % 115 == 0 or x % -115 == 0)))