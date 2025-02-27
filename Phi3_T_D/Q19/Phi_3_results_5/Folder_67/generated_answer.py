def all_ints_not_div_by_num(int_list):
    specific_ints = int_list[48:92]
    result = [x for x in specific_ints if x % 90 != 0]
    return result