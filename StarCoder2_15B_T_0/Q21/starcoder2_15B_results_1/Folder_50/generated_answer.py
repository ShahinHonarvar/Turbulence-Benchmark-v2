def all_ints_div_by_num(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 36 and i <= 46 and (num % 28 == 0)]