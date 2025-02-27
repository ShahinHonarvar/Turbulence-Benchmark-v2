def all_ints_div_by_num(int_list):
    return [num for idx, num in enumerate(int_list) if idx >= 14 and idx <= 68 and (num % 18 == 0)]