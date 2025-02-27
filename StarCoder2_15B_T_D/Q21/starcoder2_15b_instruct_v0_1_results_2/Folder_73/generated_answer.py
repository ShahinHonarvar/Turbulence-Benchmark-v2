def all_ints_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if i >= 18 and i <= 38 and (num % -97 == 0)]