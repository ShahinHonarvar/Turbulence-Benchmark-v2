def sum_ints_div_by_either_nums(lst):
    target_range = lst[81:86 + 1]
    return sum((i for i in target_range if i % -33 == 0 or i % -62 == 0))