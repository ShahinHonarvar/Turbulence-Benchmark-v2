def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[:7]) if x % -5 == 0 or x % -6 == 0))