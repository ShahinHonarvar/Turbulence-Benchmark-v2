def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 35 <= i <= 64 and (x % -30 == 0 or x % -95 == 0)))