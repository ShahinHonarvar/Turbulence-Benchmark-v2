def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[1:9], start=1) if x % -9 == 0 or x % -3 == 0))