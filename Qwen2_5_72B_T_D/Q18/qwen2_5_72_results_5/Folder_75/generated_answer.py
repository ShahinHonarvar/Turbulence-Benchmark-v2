def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[20:94]) if x % -92 == 0 or x % -50 == 0))