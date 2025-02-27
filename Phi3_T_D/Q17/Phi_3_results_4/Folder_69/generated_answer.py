def all_ints_div_by_both_two_nums(integers):
    return [integer for integer in integers[61:89] if integer % 31 == 0 and integer % 11 == 0]