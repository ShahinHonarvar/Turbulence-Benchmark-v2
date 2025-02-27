def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 14 <= i <= 93 and (x % 71 == 0 or x % 81 == 0)))