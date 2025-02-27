def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if i in (8, 9) and (x % -3 == 0 or x % 6 == 0)))