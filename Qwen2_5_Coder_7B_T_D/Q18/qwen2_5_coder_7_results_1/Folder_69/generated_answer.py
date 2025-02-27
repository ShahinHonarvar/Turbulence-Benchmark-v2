def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[61:89]) if x % 31 == 0 or x % 11 == 0))