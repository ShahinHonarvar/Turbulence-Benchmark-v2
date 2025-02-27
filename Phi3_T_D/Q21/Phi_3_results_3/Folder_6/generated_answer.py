def all_ints_div_by_num(int_list):
    return [num for i, num in enumerate(int_list[13:64], start=13) if num % 46 == 0]