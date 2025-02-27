def all_ints_div_by_num(ints_list):
    return [num for idx, num in enumerate(ints_list) if idx >= 6 and idx <= 8 and (num % -9 == 0)]