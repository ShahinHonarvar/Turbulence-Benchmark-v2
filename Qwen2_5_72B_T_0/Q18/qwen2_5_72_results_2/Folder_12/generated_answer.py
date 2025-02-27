def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[35:65], start=35) if x % -30 == 0 or x % -95 == 0))