def all_ints_not_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if i > 81 and i < 86 and (num % 77 != 0)]