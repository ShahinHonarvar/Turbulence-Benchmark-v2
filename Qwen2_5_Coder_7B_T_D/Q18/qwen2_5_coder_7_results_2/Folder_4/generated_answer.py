def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[86:91]) if x % -71 == 0 or x % -67 == 0))