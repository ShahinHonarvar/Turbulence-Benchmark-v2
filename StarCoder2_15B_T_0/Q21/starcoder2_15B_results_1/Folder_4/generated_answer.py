def all_ints_div_by_num(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 12 and i <= 92 and (num % -14 == 0)]