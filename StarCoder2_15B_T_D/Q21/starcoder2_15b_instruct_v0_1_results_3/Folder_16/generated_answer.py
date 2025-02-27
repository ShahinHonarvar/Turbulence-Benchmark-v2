def all_ints_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if i >= 13 and i <= 68 and (num % 71 == 0)]