def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 13 <= i <= 76 and (x % -66 == 0 or x % -32 == 0)))