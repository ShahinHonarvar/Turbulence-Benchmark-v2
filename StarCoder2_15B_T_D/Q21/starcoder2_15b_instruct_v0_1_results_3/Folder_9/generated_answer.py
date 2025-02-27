def all_ints_div_by_num(int_list):
    return [num for idx, num in enumerate(int_list) if idx >= 20 and idx <= 200 and (num % 4 == 0)]