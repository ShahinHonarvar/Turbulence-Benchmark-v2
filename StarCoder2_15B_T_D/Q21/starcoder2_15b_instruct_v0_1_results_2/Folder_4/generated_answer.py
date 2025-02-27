def all_ints_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if i >= 12 and i <= 92 and (num % -14 == 0)]