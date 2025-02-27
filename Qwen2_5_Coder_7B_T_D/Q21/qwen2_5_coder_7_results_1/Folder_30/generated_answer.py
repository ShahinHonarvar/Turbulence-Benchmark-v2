def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i >= 59 and i <= 79 and (num % -82 == 0)]