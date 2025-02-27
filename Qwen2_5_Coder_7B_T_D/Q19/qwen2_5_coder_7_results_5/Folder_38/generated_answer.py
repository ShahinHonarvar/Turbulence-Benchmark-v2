def all_ints_not_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if i > 32 and i < 54 and (num % -97 != 0)]