def sum_ints_div_by_either_nums(lst):
    result = sum((value for index, value in enumerate(lst) if index < 6 and (value % -5 == 0 or value % -6 == 0)))
    return result