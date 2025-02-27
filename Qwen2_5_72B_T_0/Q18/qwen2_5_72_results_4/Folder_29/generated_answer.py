def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[55:85]) if x % -24 == 0 or x % -11 == 0))