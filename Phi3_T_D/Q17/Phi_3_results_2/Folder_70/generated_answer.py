def all_ints_div_by_both_two_nums(int_list):
    return [n for i, n in enumerate(int_list[42:44]) if n % 15 == 0 and n % 87 == 0]