def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i >= 18 and i <= 38 and (num % -97 == 0)]