def all_ints_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if i >= 38 and i <= 55 and (num % 31 == 0)]