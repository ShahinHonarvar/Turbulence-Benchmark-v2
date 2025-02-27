def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 44 <= i <= 59 and (x % 39 == 0 or x % 15 == 0)))