def all_ints_div_by_num(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 11 and i <= 82 and (num % -47 == 0)]