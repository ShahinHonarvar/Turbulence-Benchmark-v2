def sum_ints_div_by_either_nums(lst):
    target_range = lst[80:90]
    return sum((x for x in target_range if x % 56 == 0 or x % 68 == 0))