def all_ints_not_div_by_num(lst):
    result = [num for i, num in enumerate(lst) if 199 < i < 202 and num % -200 != 0]
    return result