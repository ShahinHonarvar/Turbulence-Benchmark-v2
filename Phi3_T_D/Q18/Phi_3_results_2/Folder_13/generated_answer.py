def sum_ints_div_by_either_nums(lst):
    return sum((val for val in lst[13:19] if val % 45 == 0 or val % 20 == 0))