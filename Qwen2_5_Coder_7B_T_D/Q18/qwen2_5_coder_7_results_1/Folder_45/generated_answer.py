def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[30:201]) if x % -115 == 0 or x % 115 == 0))