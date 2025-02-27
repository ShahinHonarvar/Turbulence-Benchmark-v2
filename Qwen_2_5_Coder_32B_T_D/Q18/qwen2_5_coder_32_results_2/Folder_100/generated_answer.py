def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 72 <= i <= 93 and (x % 32 == 0 or x % 44 == 0)))