def all_ints_div_by_num(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 31 and i <= 67 and (num % -15 == 0)]