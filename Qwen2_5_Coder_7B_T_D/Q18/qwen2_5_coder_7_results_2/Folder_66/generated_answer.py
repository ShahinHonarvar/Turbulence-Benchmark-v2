def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[58:82]) if x % 55 == 0 or x % 10 == 0))