def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i >= 17 and i <= 63 and (num % 89 == 0)]