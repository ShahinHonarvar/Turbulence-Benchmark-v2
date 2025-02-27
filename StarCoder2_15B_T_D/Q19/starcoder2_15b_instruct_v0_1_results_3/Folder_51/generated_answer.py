def all_ints_not_div_by_num(ints_list):
    result = [num for i, num in enumerate(ints_list) if i >= 1 and i < 6 and (num % 2 != 0)]
    return result