def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i >= 11 and i <= 82 and (num % -47 == 0)]