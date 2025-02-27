def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 40 <= i <= 200 and (x % 21 == 0 or x % 71 == 0)))