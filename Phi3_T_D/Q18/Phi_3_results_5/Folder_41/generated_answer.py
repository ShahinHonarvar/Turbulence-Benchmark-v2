def sum_ints_div_by_either_nums(lst):
    return sum((val for idx, val in enumerate(lst[0:10]) if val % 6 == 0 or val % -3 == 0))