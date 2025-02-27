def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[73:87]) if x % 54 == 0 or x % 82 == 0))