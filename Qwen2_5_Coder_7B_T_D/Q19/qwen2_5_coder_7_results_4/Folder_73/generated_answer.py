def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 70 and i < 98 and (num % -88 != 0)]