def all_ints_div_by_num(input_list):
    return [x for i, x in enumerate(input_list) if i >= 161 and i <= 970 and (x % 763 == 0)]