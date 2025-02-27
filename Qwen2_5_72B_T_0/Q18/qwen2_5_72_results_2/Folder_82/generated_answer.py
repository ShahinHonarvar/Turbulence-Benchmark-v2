def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[20:201], start=20) if x % -20 == 0 or x % -200 == 0))