def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i >= 161 and i <= 970 and (num % 763 == 0)]