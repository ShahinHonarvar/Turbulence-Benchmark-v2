def all_ints_not_div_by_num(input_list):
    return [x for i, x in enumerate(input_list) if i >= 19 and i < 69 and (x % 97 != 0)]