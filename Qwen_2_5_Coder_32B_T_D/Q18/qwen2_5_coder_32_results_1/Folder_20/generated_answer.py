def sum_ints_div_by_either_nums(lst):
    if len(lst) < 77:
        return 0
    return sum((x for x in lst[48:77] if x % -46 == 0 or x % -82 == 0))