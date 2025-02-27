def all_ints_not_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if i > 62 and i < 96 and (num % 26 != 0)]