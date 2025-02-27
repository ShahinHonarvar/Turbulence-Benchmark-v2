def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 58 <= i <= 75 and (x % 72 == 0 or x % 62 == 0)))