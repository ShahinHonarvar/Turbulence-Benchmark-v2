def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 40 < i < 200 and num % 71 != 0]