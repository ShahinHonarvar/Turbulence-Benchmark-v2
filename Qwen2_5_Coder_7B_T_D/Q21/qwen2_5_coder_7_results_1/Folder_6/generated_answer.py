def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i >= 13 and i <= 63 and (num % 46 == 0)]