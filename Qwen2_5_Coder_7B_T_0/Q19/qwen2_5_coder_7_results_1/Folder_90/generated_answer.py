def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 767 and i < 905 and (num % -430 != 0)]