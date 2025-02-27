def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[48:77]) if x % -46 == 0 or x % -82 == 0))