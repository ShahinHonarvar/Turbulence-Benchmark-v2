def all_ints_not_div_by_num(ints_list):
    return [num for idx, num in enumerate(ints_list) if idx >= 103 and idx < 574 and (num % -514 != 0)]