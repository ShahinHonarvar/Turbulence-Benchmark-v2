def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[56:89]) if x % -59 == 0 or x % -79 == 0))