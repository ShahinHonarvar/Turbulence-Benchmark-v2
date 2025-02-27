def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 48 <= i <= 76 and (x % -46 == 0 or x % -82 == 0)))