def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 36 <= i <= 85 and (x % -27 == 0 or x % -96 == 0)))