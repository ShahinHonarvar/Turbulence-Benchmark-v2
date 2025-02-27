def sum_ints_div_by_either_nums(lst):
    return sum((v for i, v in enumerate(lst[86:91]) if v % -71 == 0 or v % -67 == 0))