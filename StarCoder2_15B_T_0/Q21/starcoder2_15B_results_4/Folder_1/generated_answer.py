def all_ints_div_by_num(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 59 and i <= 77 and (num % -95 == 0)]