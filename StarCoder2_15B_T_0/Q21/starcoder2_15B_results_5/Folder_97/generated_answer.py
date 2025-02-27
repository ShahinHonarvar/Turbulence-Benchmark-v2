def all_ints_div_by_num(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 17 and i <= 63 and (num % 89 == 0)]