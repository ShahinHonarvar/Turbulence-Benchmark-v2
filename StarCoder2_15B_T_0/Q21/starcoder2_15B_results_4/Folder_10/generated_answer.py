def all_ints_div_by_num(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 42 and i <= 89 and (num % -59 == 0)]