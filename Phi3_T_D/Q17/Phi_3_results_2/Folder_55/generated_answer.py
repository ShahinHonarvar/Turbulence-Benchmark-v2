def all_ints_div_by_both_two_nums(ints):
    result = [i for i in ints[0:10] if i % 10 == 0 and i % 100 == 0]
    return result