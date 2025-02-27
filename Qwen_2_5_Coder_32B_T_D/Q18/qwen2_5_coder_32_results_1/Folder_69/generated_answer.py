def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 61 <= i <= 88 and (x % 31 == 0 or x % 11 == 0)))