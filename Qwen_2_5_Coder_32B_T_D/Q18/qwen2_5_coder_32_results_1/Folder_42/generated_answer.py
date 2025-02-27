def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 29 <= i <= 45 and (x % 27 == 0 or x % 81 == 0)))