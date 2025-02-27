def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 20 and i < 43 and (num % 95 != 0)]