def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 1 <= i <= 4 and (x % 4 == 0 or x % -6 == 0)))