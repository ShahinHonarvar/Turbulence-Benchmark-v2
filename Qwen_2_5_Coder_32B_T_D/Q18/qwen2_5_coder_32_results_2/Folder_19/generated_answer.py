def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if i in range(1, 5) and (x % 4 == 0 or x % -6 == 0)))