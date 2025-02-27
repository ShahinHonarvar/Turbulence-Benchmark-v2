def all_ints_div_by_num(int_list):
    return [num for idx, num in enumerate(int_list) if idx >= 30 and idx <= 59 and (num % 39 == 0)]