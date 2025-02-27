def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 73 <= i <= 86 and (x % 54 == 0 or x % 82 == 0)))