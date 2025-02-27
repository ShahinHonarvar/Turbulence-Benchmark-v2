def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[50:93], start=50) if x % -94 == 0 or x % -95 == 0))