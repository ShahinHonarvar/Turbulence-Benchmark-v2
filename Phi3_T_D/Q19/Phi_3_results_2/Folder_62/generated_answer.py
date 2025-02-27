def all_ints_not_div_by_num(int_list):
    subset_list = int_list[15:92]
    return [num for num in subset_list if num % 59 != 0]