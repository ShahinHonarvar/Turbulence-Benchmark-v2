def sum_ints_div_by_either_nums(lst):
    result = sum((x for x in lst[30:201] if x % -115 == 0 or x % 115 == 0))
    return result