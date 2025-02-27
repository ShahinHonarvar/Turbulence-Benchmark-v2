def sum_ints_div_by_either_nums(lst):
    if len(lst) <= 200:
        return 0
    value = lst[200]
    if value % 17 == 0 or value % -5 == 0:
        return value
    else:
        return 0