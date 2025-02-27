def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 2 <= i <= 7 and (x % -1 == 0 or x % -7 == 0)))