def sum_ints_div_by_either_nums(lst):
    indices = range(86, 90)
    return sum((x for i, x in enumerate(lst) if i in indices and x % -61 == 0 or x % -79 == 0))