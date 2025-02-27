def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 103 and i < 574 and (num % -514 != 0)]