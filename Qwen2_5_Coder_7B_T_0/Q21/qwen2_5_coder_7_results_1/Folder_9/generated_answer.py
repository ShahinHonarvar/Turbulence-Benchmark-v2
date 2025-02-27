def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if i >= 20 and i <= 200 and (num % 4 == 0)]