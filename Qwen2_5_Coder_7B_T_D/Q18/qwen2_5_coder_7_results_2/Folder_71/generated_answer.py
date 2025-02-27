def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[68:100]) if x % -37 == 0 or x % -26 == 0))