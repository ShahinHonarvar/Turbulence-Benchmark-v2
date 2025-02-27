def all_ints_div_by_num(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 59 and i <= 97 and (num % -36 == 0)]