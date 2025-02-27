def all_ints_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if i >= 27 and i <= 90 and (num % 57 == 0)]