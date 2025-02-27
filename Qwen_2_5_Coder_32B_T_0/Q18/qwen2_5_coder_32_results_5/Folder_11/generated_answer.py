def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 22 <= i <= 24 and (x % -85 == 0 or x % -30 == 0)))