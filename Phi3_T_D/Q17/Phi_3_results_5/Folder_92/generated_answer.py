def all_ints_div_by_both_two_nums(integers):
    return [integer for integer in integers[:1] if integer % 1 == 0 and integer % -1 == 0]