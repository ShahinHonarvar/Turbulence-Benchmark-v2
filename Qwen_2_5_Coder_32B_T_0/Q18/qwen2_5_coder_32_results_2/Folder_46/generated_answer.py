def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 11 <= i <= 46 and (x % 55 == 0 or x % 36 == 0)))