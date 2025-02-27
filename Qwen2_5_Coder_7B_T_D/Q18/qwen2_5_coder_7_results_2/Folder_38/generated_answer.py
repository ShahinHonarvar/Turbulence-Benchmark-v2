def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if (i >= 10 and i <= 76) and (x % -40 == 0 or x % -12 == 0)))