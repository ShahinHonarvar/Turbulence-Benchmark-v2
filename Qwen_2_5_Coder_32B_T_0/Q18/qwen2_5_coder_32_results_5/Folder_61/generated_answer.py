def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[:7]) if i <= 6 and (x % -5 == 0 or x % -6 == 0)))