def all_ints_div_by_both_two_nums(ints):
    range_start, range_end = (51, 76)
    divisible_ints = [x for x in ints[range_start:range_end + 1] if x % -90 == 0 and x % -59 == 0]
    return divisible_ints