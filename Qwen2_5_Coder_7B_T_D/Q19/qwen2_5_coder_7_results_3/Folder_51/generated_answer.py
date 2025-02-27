def all_ints_not_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if i > 1 and i < 6 and (num % 2 != 0)]