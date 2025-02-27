def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[50:93]) if i % 2 == 0 and (x % -94 == 0 or x % -95 == 0)))