def all_ints_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if i >= 5 and i <= 6 and (num % -6 == 0)]