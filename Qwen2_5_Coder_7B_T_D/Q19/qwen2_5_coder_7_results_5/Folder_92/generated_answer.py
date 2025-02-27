def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i not in [0, 1] and num % -1 != 0]