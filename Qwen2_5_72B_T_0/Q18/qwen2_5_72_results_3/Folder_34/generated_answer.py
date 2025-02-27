def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[60:201]) if x % 9 == 0 or x % 11 == 0))