def sum_ints_div_by_either_nums(int_list):
    sliced_list = int_list[8:10]
    return sum((x for x in sliced_list if x % -3 == 0 or x % 6 == 0))