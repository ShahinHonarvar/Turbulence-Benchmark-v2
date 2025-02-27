def all_ints_div_by_both_two_nums(int_list):
    divisible_ints = [i for i in int_list[68:99 + 1] if i % -37 == 0 and i % -26 == 0]
    return divisible_ints