def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[25:81]) if i % 1 == 0 and (x % -20 == 0 or x % -26 == 0)))