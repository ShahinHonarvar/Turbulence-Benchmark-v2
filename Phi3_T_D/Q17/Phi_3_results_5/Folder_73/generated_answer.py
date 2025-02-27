def all_ints_div_by_both_two_nums(list_of_ints):
    divisible_by_both = [value for index, value in enumerate(list_of_ints[80:86]) if value % -33 == 0 and value % -62 == 0]
    return divisible_by_both