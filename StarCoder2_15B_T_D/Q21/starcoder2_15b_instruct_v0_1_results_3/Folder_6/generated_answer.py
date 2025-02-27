def all_ints_div_by_num(input_list):
    return [num for i, num in enumerate(input_list) if i >= 13 and i <= 63 and (num % 46 == 0)]