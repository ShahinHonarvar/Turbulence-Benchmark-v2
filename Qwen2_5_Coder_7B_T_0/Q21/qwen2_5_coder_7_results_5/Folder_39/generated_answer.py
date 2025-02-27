def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i >= 10 and i <= 52 and (num % -12 == 0)]