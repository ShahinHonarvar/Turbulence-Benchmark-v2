def all_ints_div_by_both_two_nums(input_list):
    result = [x for x in input_list if x % 67 == 0 and x % 15 == 0]
    return result[46:92]