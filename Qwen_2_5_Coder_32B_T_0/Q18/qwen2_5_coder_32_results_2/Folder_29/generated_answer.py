def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 55 <= i <= 84 and (x % -24 == 0 or x % -11 == 0)))