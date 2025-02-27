def sum_ints_div_by_either_nums(ints_list):
    return sum((i for i in ints_list[25:96] if i % 51 == 0 or i % 77 == 0))