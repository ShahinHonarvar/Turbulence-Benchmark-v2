def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[154:800]) if x % 275 == 0 or x % 580 == 0))