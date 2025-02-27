def sum_ints_div_by_either_nums(ints):
    return sum((x for x in ints[200:201] if x % 17 == 0 or x % -5 == 0))