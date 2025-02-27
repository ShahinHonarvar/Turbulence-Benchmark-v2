def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 33 and i < 78 and (num % -17 != 0)]