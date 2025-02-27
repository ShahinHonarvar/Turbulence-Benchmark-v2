def all_ints_not_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if i >= 21 and i < 51 and (num % -77 != 0)]