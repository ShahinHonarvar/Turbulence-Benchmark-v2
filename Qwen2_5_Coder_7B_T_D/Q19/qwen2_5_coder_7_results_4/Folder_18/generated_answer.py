def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 35 and i < 98 and (num % 41 != 0)]