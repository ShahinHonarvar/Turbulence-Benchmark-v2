def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 6 <= i <= 9 and (x % -1 == 0 or x % -10 == 0)))