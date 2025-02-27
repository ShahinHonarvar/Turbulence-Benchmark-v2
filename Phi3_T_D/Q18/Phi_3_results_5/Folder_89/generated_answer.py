def sum_ints_div_by_either_nums(int_list):
    return sum((int_list[28:97] if len(int_list) >= 97 else int_list[28:] for i in int_list[28:] if i % 90 == 0 or i % 97 == 0))