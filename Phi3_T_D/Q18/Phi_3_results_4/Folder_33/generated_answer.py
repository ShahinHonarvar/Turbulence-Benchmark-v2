def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[281:695]) if x % -722 == 0 or x % -731 == 0)) or 0