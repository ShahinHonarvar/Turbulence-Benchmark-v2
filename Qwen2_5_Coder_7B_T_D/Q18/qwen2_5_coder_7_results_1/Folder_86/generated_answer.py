def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if (i >= 54 and i <= 79) and (x % 54 == 0 or x % 28 == 0)))