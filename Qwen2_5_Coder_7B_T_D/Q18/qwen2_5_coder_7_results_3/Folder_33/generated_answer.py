def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if (i >= 281 and i <= 694) and (x % -722 == 0 or x % -731 == 0)))