def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i > 3 and i < 9 and (num % 6 != 0)]