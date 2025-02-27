def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 63 and i < 73 and (num % -99 != 0)]