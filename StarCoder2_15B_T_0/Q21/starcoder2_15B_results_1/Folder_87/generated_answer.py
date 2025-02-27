def all_ints_div_by_num(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 10 and i <= 56 and (num % 16 == 0)]