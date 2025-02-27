def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 21 < i < 69 and num % -69 != 0]