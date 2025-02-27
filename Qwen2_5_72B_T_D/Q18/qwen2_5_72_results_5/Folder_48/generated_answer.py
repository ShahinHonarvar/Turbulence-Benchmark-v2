def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[306:958], start=306) if x % 982 == 0 or x % 319 == 0))