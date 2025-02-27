def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[2:8]) if x % -1 == 0 or x % -7 == 0))