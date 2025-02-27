def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[:2]) if x % -6 == 0 or x % 4 == 0))