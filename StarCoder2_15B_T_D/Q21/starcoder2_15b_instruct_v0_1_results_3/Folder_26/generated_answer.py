def all_ints_div_by_num(ints_list):
    return [num for i, num in enumerate(ints_list) if i >= 45 and i <= 80 and (num % 39 == 0)]