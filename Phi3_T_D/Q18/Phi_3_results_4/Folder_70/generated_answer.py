def sum_ints_div_by_either_nums(lst):
    return sum((val for i, val in enumerate(lst[42:44]) if val % 15 == 0 or val % 87 == 0))