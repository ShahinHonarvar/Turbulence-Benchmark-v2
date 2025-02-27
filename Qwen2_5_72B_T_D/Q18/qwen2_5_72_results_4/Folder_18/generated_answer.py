def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[55:67]) if x % 22 == 0 or x % 82 == 0))