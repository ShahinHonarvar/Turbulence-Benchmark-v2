def all_ints_not_div_by_num(input_list):
    return [num for i, num in enumerate(input_list) if i >= 16 and i < 87 and (num % -15 != 0)]