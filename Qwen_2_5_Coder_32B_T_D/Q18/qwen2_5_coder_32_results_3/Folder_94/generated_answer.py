def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if i in (93, 94) and (x % -53 == 0 or x % -91 == 0)))