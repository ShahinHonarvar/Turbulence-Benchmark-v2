def all_ints_div_by_both_two_nums(int_list):
    divisible_ints = [x for x in int_list[77:88] if x % 23 == 0 and x % 57 == 0]
    return divisible_ints