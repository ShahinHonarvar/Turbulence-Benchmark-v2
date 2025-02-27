def all_ints_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if i >= 10 and i <= 52 and (num % -12 == 0)]