def all_ints_div_by_both_two_nums(ints):
    divisible_ints = [i for i in ints[10:80] if i % -74 == 0 and i % -58 == 0]
    return divisible_ints