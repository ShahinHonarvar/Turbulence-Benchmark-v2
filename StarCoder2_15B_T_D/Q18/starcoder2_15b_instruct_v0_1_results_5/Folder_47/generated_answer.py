def sum_ints_div_by_either_nums(ints):
    return sum((x for x in ints[42:88] if x % -90 == 0 or x % -74 == 0))