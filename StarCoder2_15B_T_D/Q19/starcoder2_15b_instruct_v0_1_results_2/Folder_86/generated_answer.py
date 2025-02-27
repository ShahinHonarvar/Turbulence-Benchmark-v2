def all_ints_not_div_by_num(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 15 and i < 63 and (num % 34 != 0)]