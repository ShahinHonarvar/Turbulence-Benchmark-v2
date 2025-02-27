def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if i in range(2) and (x % -6 == 0 or x % 4 == 0)))