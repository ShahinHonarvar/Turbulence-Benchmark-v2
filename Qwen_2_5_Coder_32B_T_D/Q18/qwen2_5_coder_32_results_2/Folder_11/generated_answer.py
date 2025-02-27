def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if i in range(22, 25) and (x % -85 == 0 or x % -30 == 0)))