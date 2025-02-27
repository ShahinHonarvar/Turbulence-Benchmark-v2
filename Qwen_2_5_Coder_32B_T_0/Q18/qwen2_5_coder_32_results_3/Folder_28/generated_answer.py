def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 34 <= i <= 81 and (x % 27 == 0 or x % 57 == 0)))