def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 32 <= i <= 99 and (x % -11 == 0 or x % -15 == 0)))