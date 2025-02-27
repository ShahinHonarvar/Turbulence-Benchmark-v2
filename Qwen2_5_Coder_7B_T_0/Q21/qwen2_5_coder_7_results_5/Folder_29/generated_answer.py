def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i >= 52 and i <= 72 and (num % -15 == 0)]