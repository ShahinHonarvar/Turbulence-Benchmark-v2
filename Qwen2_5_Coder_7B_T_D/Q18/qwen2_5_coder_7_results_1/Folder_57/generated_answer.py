def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if i in range(51, 77) and (x % -90 == 0 or x % -59 == 0)))