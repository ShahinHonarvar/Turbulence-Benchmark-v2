def all_ints_not_div_by_num(lst):
    return [num for index, num in enumerate(lst) if index > 22 and index < 97 and (num % -46 != 0)]