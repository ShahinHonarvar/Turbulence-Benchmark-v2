def sum_ints_div_by_either_nums(ints):
    return sum((x for x in ints[70:201] if x % 3 == 0 or x % -300 == 0))