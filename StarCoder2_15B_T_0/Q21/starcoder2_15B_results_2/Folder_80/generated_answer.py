def all_ints_div_by_num(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 27 and i <= 86 and (num % 29 == 0)]