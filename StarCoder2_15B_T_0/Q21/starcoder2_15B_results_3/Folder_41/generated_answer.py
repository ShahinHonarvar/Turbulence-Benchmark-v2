def all_ints_div_by_num(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 0 and i <= 5 and (num % 5 == 0)]